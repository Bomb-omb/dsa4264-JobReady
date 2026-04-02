import argparse
import io
import unittest
from unittest import mock
from pathlib import Path

import pandas as pd

import extract_skillsfuture_course as course


def make_args(**overrides: object) -> argparse.Namespace:
    values = {
        "input_file": "data/2025-2026_module_clean_with_prereq.csv",
        "output_file": None,
        "id_column": "moduleCode",
        "text_column": "description",
        "output_column": "extracted_skills",
        "apps_tools_column": "extracted_apps_tools",
        "status_column": "done",
        "row_index": None,
        "row_count": None,
        "force": False,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class ExtractSkillsFutureCourseTests(unittest.TestCase):
    def write_temp_download_file(self, content: str) -> Path:
        file_path = Path(f"tmp_{self._testMethodName}.csv")
        file_path.write_text(content, encoding="utf-8")
        self.addCleanup(lambda: file_path.unlink(missing_ok=True))
        return file_path

    def test_ensure_output_columns_adds_missing_columns(self) -> None:
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                }
            ]
        )

        result = course.ensure_output_columns(df, make_args())

        self.assertIn("extracted_skills", result.columns)
        self.assertIn("extracted_apps_tools", result.columns)
        self.assertIn("done", result.columns)
        self.assertEqual(result.at[0, "extracted_skills"], "")
        self.assertEqual(result.at[0, "extracted_apps_tools"], "")
        self.assertEqual(result.at[0, "done"], "")

    def test_build_output_path_defaults_to_input_path(self) -> None:
        input_path = Path("data/2025-2026_module_clean_with_prereq.csv")

        result = course.build_output_path(input_path, output_file=None)

        self.assertEqual(result, input_path)

    def test_normalize_status_value_defaults_pending(self) -> None:
        self.assertEqual(course.normalize_status_value(None), "pending")
        self.assertEqual(course.normalize_status_value(""), "pending")
        self.assertEqual(course.normalize_status_value(" success "), "success")

    def test_extract_section_from_csv_preserves_commas_in_skill_names(self) -> None:
        content = "\n".join(
            [
                "input_text",
                "Example description",
                "extracted_skills",
                "Event Logistics Administration; Tags: Others",
                (
                    "Meetings, Incentives, Conferences and Exhibitions (MICE) "
                    "Content and Experience Development and Delivery; Tags: Others"
                ),
                "extracted_apps_and_tools",
                "Python; Tags: Tool",
            ]
        )

        file_path = self.write_temp_download_file(content)
        result = course.extract_section_from_csv(file_path, course.SKILLS_SECTION_HEADER)

        self.assertEqual(
            result,
            "Event Logistics Administration | Meetings, Incentives, Conferences and "
            "Exhibitions (MICE) Content and Experience Development and Delivery",
        )

    def test_extract_section_from_csv_handles_multiple_comma_containing_skills(self) -> None:
        content = "\n".join(
            [
                "extracted_skills",
                (
                    "Meetings, Incentives, Conferences and Exhibitions (MICE) "
                    "Content and Experience Development and Delivery; Tags: Others"
                ),
                "Tour and Travel Coordination, Ticketing and Reservations Management; Tags: CASL",
                "Events Planning and Management; Tags: Others",
            ]
        )

        file_path = self.write_temp_download_file(content)
        result = course.extract_section_from_csv(file_path, course.SKILLS_SECTION_HEADER)

        self.assertEqual(
            result,
            "Meetings, Incentives, Conferences and Exhibitions (MICE) Content and "
            "Experience Development and Delivery | Tour and Travel Coordination, "
            "Ticketing and Reservations Management | Events Planning and Management",
        )

    def test_extract_section_from_csv_deduplicates_lines_while_preserving_order(self) -> None:
        content = "\n".join(
            [
                "extracted_skills",
                "Data Strategy; Tags: Emerging",
                "Tour and Travel Coordination, Ticketing and Reservations Management; Tags: CASL",
                "Data Strategy; Tags: Emerging",
            ]
        )

        file_path = self.write_temp_download_file(content)
        result = course.extract_section_from_csv(file_path, course.SKILLS_SECTION_HEADER)

        self.assertEqual(
            result,
            "Data Strategy | Tour and Travel Coordination, Ticketing and Reservations Management",
        )

    def test_run_extraction_for_text_rejects_empty_text(self) -> None:
        success, partial_results, error_message, error_count = course.run_extraction_for_text(
            identifier="CS1010",
            text="   ",
            args=make_args(),
            error_count=3,
        )

        self.assertFalse(success)
        self.assertEqual(partial_results, {})
        self.assertEqual(error_message, "Text to extract is empty.")
        self.assertEqual(error_count, 3)

    def test_run_extraction_for_text_returns_partial_results_on_failure(self) -> None:
        args = make_args()

        with (
            mock.patch.object(course, "paste_text"),
            mock.patch.object(course, "click_result_tab"),
            mock.patch.object(
                course,
                "click_download_and_read",
                side_effect=["Programming", RuntimeError("Apps & Tools download failed.")],
            ) as download_mock,
            mock.patch.object(course, "reset_page") as reset_mock,
            mock.patch.object(course.time, "sleep"),
        ):
            success, partial_results, error_message, error_count = course.run_extraction_for_text(
                identifier="CS1010",
                text="Intro programming",
                args=args,
                error_count=0,
            )

        self.assertFalse(success)
        self.assertEqual(partial_results, {"extracted_skills": "Programming"})
        self.assertEqual(error_message, "Apps & Tools download failed.")
        self.assertEqual(error_count, 1)
        self.assertEqual(download_mock.call_count, 2)
        reset_mock.assert_called_once()

    def test_run_extraction_for_text_checks_apps_tools_after_skills_failure(self) -> None:
        args = make_args()

        with (
            mock.patch.object(course, "paste_text"),
            mock.patch.object(course, "click_result_tab") as tab_mock,
            mock.patch.object(
                course,
                "click_download_and_read",
                side_effect=[RuntimeError("Skills download failed."), "Python"],
            ) as download_mock,
            mock.patch.object(course, "reset_page") as reset_mock,
            mock.patch.object(course.time, "sleep"),
        ):
            success, partial_results, error_message, error_count = course.run_extraction_for_text(
                identifier="CS1010",
                text="Intro programming",
                args=args,
                error_count=0,
            )

        self.assertFalse(success)
        self.assertEqual(partial_results, {"extracted_apps_tools": "Python"})
        self.assertEqual(error_message, "Skills download failed.")
        self.assertEqual(error_count, 1)
        self.assertEqual(tab_mock.call_count, 2)
        self.assertEqual(download_mock.call_count, 2)
        reset_mock.assert_called_once()

    def test_run_extraction_for_text_prefers_skills_error_when_both_tabs_fail(self) -> None:
        args = make_args()

        with (
            mock.patch.object(course, "paste_text"),
            mock.patch.object(course, "click_result_tab"),
            mock.patch.object(
                course,
                "click_download_and_read",
                side_effect=[
                    RuntimeError("Skills download failed."),
                    RuntimeError("Apps & Tools download failed."),
                ],
            ) as download_mock,
            mock.patch.object(course, "reset_page") as reset_mock,
            mock.patch.object(course.time, "sleep"),
        ):
            success, partial_results, error_message, error_count = course.run_extraction_for_text(
                identifier="CS1010",
                text="Intro programming",
                args=args,
                error_count=0,
            )

        self.assertFalse(success)
        self.assertEqual(partial_results, {})
        self.assertEqual(error_message, "Skills download failed.")
        self.assertEqual(error_count, 1)
        self.assertEqual(download_mock.call_count, 2)
        reset_mock.assert_called_once()

    def test_run_extraction_for_text_refreshes_and_resets_error_count_at_threshold(self) -> None:
        args = make_args()

        with (
            mock.patch.object(course, "paste_text"),
            mock.patch.object(course, "click_result_tab"),
            mock.patch.object(
                course,
                "click_download_and_read",
                side_effect=RuntimeError("Skills download failed."),
            ),
            mock.patch.object(course, "refresh_website") as refresh_mock,
            mock.patch.object(course, "reset_page") as reset_mock,
            mock.patch.object(course.time, "sleep"),
        ):
            success, partial_results, error_message, error_count = course.run_extraction_for_text(
                identifier="CS1010",
                text="Intro programming",
                args=args,
                error_count=course.ERROR_REFRESH_THRESHOLD - 1,
            )

        self.assertFalse(success)
        self.assertEqual(partial_results, {})
        self.assertEqual(error_message, "Skills download failed.")
        self.assertEqual(error_count, 0)
        refresh_mock.assert_called_once()
        self.assertEqual(reset_mock.call_count, 2)

    def test_apply_unique_results_maps_duplicate_descriptions(self) -> None:
        args = make_args()
        full_df = pd.DataFrame(
            [
                {
                    "moduleCode": "ACC1701",
                    "description": "Same description",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
                {
                    "moduleCode": "ACC1701A",
                    "description": "Same description",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
                {
                    "moduleCode": "CS1010",
                    "description": "Other description",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
            ]
        )
        unique_df = pd.DataFrame(
            [
                {
                    "moduleCode": "ACC1701",
                    "description": "Same description",
                    "extracted_skills": "Accounting",
                    "extracted_apps_tools": "Excel",
                    "done": "success",
                },
                {
                    "moduleCode": "CS1010",
                    "description": "Other description",
                    "extracted_skills": "Programming",
                    "extracted_apps_tools": "",
                    "done": "success",
                },
            ]
        )

        result = course.apply_unique_results_to_full_dataframe(full_df, unique_df, args)

        self.assertEqual(result.at[0, "extracted_skills"], "Accounting")
        self.assertEqual(result.at[1, "extracted_skills"], "Accounting")
        self.assertEqual(result.at[0, "extracted_apps_tools"], "Excel")
        self.assertEqual(result.at[1, "done"], "success")
        self.assertEqual(result.at[2, "extracted_skills"], "Programming")

    def test_validate_args_accepts_row_index_without_row_count(self) -> None:
        args = make_args(row_index=3)

        course.validate_args(args)

    def test_validate_args_rejects_row_index_with_row_count(self) -> None:
        args = make_args(row_index=3, row_count=5)

        with self.assertRaisesRegex(SystemExit, "--row-index cannot be used with --row-count"):
            course.validate_args(args)

    def test_validate_args_requires_row_count_without_row_index(self) -> None:
        args = make_args()

        with self.assertRaisesRegex(SystemExit, "--row-count is required unless --row-index is used"):
            course.validate_args(args)

    def test_validate_args_rejects_non_positive_row_count(self) -> None:
        args = make_args(row_count=0)

        with self.assertRaisesRegex(SystemExit, "--row-count must be a positive integer"):
            course.validate_args(args)

    def test_resolve_load_and_output_paths_defaults_to_input_file(self) -> None:
        temp_path = Path("tmp_path_resolution")
        input_path = temp_path / "modules.csv"

        with mock.patch.object(Path, "exists", autospec=True) as exists_mock:
            exists_mock.side_effect = lambda self: self == input_path
            load_path, resolved_output_path = course.resolve_load_and_output_paths(
                input_path,
                make_args(row_count=5),
            )

        self.assertEqual(load_path, input_path)
        self.assertEqual(resolved_output_path, input_path)

    def test_resolve_load_and_output_paths_bootstraps_from_input_when_output_missing(self) -> None:
        temp_path = Path("tmp_path_resolution")
        input_path = temp_path / "modules.csv"
        explicit_output = temp_path / "custom.csv"

        with mock.patch.object(Path, "exists", autospec=True, return_value=False):
            load_path, output_path = course.resolve_load_and_output_paths(
                input_path,
                make_args(row_count=5, output_file=str(explicit_output)),
            )

        self.assertEqual(load_path, input_path)
        self.assertEqual(output_path, explicit_output)

    def test_resolve_load_and_output_paths_honors_explicit_output_file(self) -> None:
        temp_path = Path("tmp_path_resolution")
        input_path = temp_path / "modules.csv"
        explicit_output = temp_path / "custom.csv"

        with mock.patch.object(Path, "exists", autospec=True) as exists_mock:
            exists_mock.side_effect = lambda self: self == explicit_output
            load_path, output_path = course.resolve_load_and_output_paths(
                input_path,
                make_args(
                    row_count=5,
                    output_file=str(explicit_output),
                ),
            )

        self.assertEqual(load_path, explicit_output)
        self.assertEqual(output_path, explicit_output)

    def test_resolve_batch_row_window_starts_at_first_pending_row(self) -> None:
        df = pd.DataFrame(
            [
                {"moduleCode": "ACC1701", "description": "A", "done": "success"},
                {"moduleCode": "CS1010", "description": "B", "done": "pending"},
                {"moduleCode": "CS1010E", "description": "C", "done": "pending"},
            ]
        )

        start_row, end_row = course.resolve_batch_row_window(
            df,
            make_args(row_count=1),
        )

        self.assertEqual(start_row, 1)
        self.assertEqual(end_row, 2)

    def test_resolve_batch_row_window_caps_at_end_of_file(self) -> None:
        df = pd.DataFrame(
            [
                {"moduleCode": "ACC1701", "description": "A", "done": "success"},
                {"moduleCode": "CS1010", "description": "B", "done": "pending"},
                {"moduleCode": "CS2030", "description": "C", "done": "pending"},
            ]
        )

        start_row, end_row = course.resolve_batch_row_window(
            df,
            make_args(row_count=10),
        )

        self.assertEqual(start_row, 1)
        self.assertEqual(end_row, 3)

    def test_resolve_batch_row_window_returns_none_when_no_pending_rows(self) -> None:
        df = pd.DataFrame(
            [
                {"moduleCode": "ACC1701", "description": "A", "done": "success"},
                {"moduleCode": "CS1010", "description": "B", "done": "error: failed"},
            ]
        )

        start_row, end_row = course.resolve_batch_row_window(
            df,
            make_args(row_count=10),
        )

        self.assertIsNone(start_row)
        self.assertIsNone(end_row)

    def test_resolve_batch_row_window_ignores_earlier_error_rows(self) -> None:
        df = pd.DataFrame(
            [
                {"moduleCode": "ACC1701", "description": "A", "done": "error: failed"},
                {"moduleCode": "CS1010", "description": "B", "done": "pending"},
                {"moduleCode": "CS2030", "description": "C", "done": "success"},
            ]
        )

        start_row, end_row = course.resolve_batch_row_window(
            df,
            make_args(row_count=2),
        )

        self.assertEqual(start_row, 1)
        self.assertEqual(end_row, 3)

    def test_apply_unique_results_to_row_subset_keeps_outside_rows_unchanged(self) -> None:
        args = make_args()
        full_df = pd.DataFrame(
            [
                {
                    "moduleCode": "ACC1701",
                    "description": "Same description",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
                {
                    "moduleCode": "ACC1701A",
                    "description": "Same description",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
                {
                    "moduleCode": "CS1010",
                    "description": "Other description",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
            ]
        )
        unique_df = pd.DataFrame(
            [
                {
                    "moduleCode": "ACC1701A",
                    "description": "Same description",
                    "extracted_skills": "Accounting",
                    "extracted_apps_tools": "Excel",
                    "done": "success",
                },
                {
                    "moduleCode": "CS1010",
                    "description": "Other description",
                    "extracted_skills": "Programming",
                    "extracted_apps_tools": "",
                    "done": "success",
                },
            ],
            index=[1, 2],
        )

        course.apply_unique_results_to_row_subset(full_df, full_df.index[1:3], unique_df, args)

        self.assertEqual(full_df.at[0, "extracted_skills"], "")
        self.assertEqual(full_df.at[0, "done"], "pending")
        self.assertEqual(full_df.at[1, "extracted_skills"], "Accounting")
        self.assertEqual(full_df.at[2, "extracted_skills"], "Programming")

    def test_process_single_row_writes_error_status_and_partial_results(self) -> None:
        args = make_args(row_index=0)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                }
            ]
        )
        input_path = Path("data/modules.csv")
        output_path = Path("data/modules_skillsfuture.csv")

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                return_value=(
                    False,
                    {"extracted_skills": "Programming"},
                    "Skills download failed.",
                    1,
                ),
            ) as run_mock,
            mock.patch.object(course, "save_dataframe") as save_mock,
        ):
            course.process_single_row(df, args, input_path, output_path)

        self.assertEqual(df.at[0, "extracted_skills"], "Programming")
        self.assertEqual(df.at[0, "extracted_apps_tools"], "")
        self.assertEqual(df.at[0, "done"], "error: Skills download failed.")
        run_mock.assert_called_once_with(
            identifier="CS1010",
            text="Intro programming",
            args=args,
            error_count=0,
        )
        save_mock.assert_called_once_with(df, input_path, output_path)

    def test_process_single_row_writes_apps_tools_partial_results_on_skills_error(self) -> None:
        args = make_args(row_index=0)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                }
            ]
        )

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                return_value=(
                    False,
                    {"extracted_apps_tools": "Python"},
                    "Skills download failed.",
                    1,
                ),
            ),
            mock.patch.object(course, "save_dataframe"),
        ):
            course.process_single_row(df, args, Path("in.csv"), Path("out.csv"))

        self.assertEqual(df.at[0, "extracted_skills"], "")
        self.assertEqual(df.at[0, "extracted_apps_tools"], "Python")
        self.assertEqual(df.at[0, "done"], "error: Skills download failed.")

    def test_process_single_row_writes_success_status(self) -> None:
        args = make_args(row_index=0)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                }
            ]
        )

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                return_value=(
                    True,
                    {
                        "extracted_skills": "Programming",
                        "extracted_apps_tools": "Python",
                    },
                    "",
                    0,
                ),
            ),
            mock.patch.object(course, "save_dataframe"),
        ):
            course.process_single_row(df, args, Path("in.csv"), Path("out.csv"))

        self.assertEqual(df.at[0, "extracted_skills"], "Programming")
        self.assertEqual(df.at[0, "extracted_apps_tools"], "Python")
        self.assertEqual(df.at[0, "done"], "success")

    def test_process_single_row_prints_only_row_index_and_save_path_on_success(self) -> None:
        args = make_args(row_index=0)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                }
            ]
        )

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                return_value=(
                    True,
                    {
                        "extracted_skills": "Programming",
                        "extracted_apps_tools": "Python",
                    },
                    "",
                    0,
                ),
            ),
            mock.patch.object(course, "save_dataframe"),
            mock.patch("sys.stdout", new_callable=io.StringIO) as stdout,
        ):
            course.process_single_row(df, args, Path("in.csv"), Path("out.csv"))

        self.assertEqual(
            stdout.getvalue().strip().splitlines(),
            [
                "Processing physical row index 0",
                "Saved output to: out.csv",
            ],
        )

    def test_process_single_row_prints_single_error_line_on_failure(self) -> None:
        args = make_args(row_index=0)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                }
            ]
        )

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                return_value=(
                    False,
                    {"extracted_skills": "Programming"},
                    "Skills download failed.",
                    1,
                ),
            ),
            mock.patch.object(course, "save_dataframe"),
            mock.patch("sys.stdout", new_callable=io.StringIO) as stdout,
        ):
            course.process_single_row(df, args, Path("in.csv"), Path("out.csv"))

        self.assertEqual(
            stdout.getvalue().strip().splitlines(),
            [
                "Processing physical row index 0",
                "Error on row 0: Skills download failed.",
                "Saved output to: out.csv",
            ],
        )

    def test_process_batch_rows_passes_shared_error_count_between_rows(self) -> None:
        args = make_args(row_count=2)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "ACC1701",
                    "description": "Accounting basics",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
            ]
        )

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                side_effect=[
                    (False, {"extracted_skills": "Accounting"}, "First row failed.", 1),
                    (
                        True,
                        {
                            "extracted_skills": "Programming",
                            "extracted_apps_tools": "Python",
                        },
                        "",
                        0,
                    ),
                ],
            ) as run_mock,
            mock.patch.object(course, "save_dataframe") as save_mock,
        ):
            course.process_batch_rows(df, args, Path("in.csv"), Path("out.csv"), 0, 2)

        self.assertEqual(df.at[0, "extracted_skills"], "Accounting")
        self.assertEqual(df.at[0, "done"], "error: First row failed.")
        self.assertEqual(df.at[1, "extracted_skills"], "Programming")
        self.assertEqual(df.at[1, "extracted_apps_tools"], "Python")
        self.assertEqual(df.at[1, "done"], "success")
        self.assertEqual(save_mock.call_count, 2)
        self.assertEqual(
            [call.kwargs["error_count"] for call in run_mock.call_args_list],
            [0, 1],
        )

    def test_process_batch_rows_prints_only_row_window_error_and_save_path(self) -> None:
        args = make_args(row_count=2)
        df = pd.DataFrame(
            [
                {
                    "moduleCode": "ACC1701",
                    "description": "Accounting basics",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
                {
                    "moduleCode": "CS1010",
                    "description": "Intro programming",
                    "extracted_skills": "",
                    "extracted_apps_tools": "",
                    "done": "pending",
                },
            ]
        )

        with (
            mock.patch.object(
                course,
                "run_extraction_for_text",
                side_effect=[
                    (False, {"extracted_skills": "Accounting"}, "First row failed.", 1),
                    (
                        True,
                        {
                            "extracted_skills": "Programming",
                            "extracted_apps_tools": "Python",
                        },
                        "",
                        0,
                    ),
                ],
            ),
            mock.patch.object(course, "save_dataframe"),
            mock.patch("sys.stdout", new_callable=io.StringIO) as stdout,
        ):
            course.process_batch_rows(df, args, Path("in.csv"), Path("out.csv"), 0, 2)

        lines = stdout.getvalue().strip().splitlines()
        self.assertEqual(
            lines,
            [
                "Processing physical rows 0 to 1",
                "Error on row 0: First row failed.",
                "Saved output to: out.csv",
            ],
        )
        self.assertNotIn("Processing batch unique row", stdout.getvalue())
        self.assertNotIn("Unique descriptions to process in batch", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
