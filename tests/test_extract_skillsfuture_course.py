import argparse
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
        "start_course_code": None,
        "row_count": None,
        "in_place": False,
        "force": False,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class ExtractSkillsFutureCourseTests(unittest.TestCase):
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

    def test_build_output_path_defaults_to_skillsfuture_suffix(self) -> None:
        input_path = Path("data/2025-2026_module_clean_with_prereq.csv")

        result = course.build_output_path(input_path, output_file=None, in_place=False)

        self.assertEqual(
            result,
            Path("data/2025-2026_module_clean_with_prereq_skillsfuture.csv"),
        )

    def test_normalize_status_value_defaults_pending(self) -> None:
        self.assertEqual(course.normalize_status_value(None), "pending")
        self.assertEqual(course.normalize_status_value(""), "pending")
        self.assertEqual(course.normalize_status_value(" success "), "success")

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

    def test_validate_args_accepts_start_course_code_with_row_count(self) -> None:
        args = make_args(start_course_code="CS1010", row_count=5)

        course.validate_args(args)

    def test_validate_args_rejects_row_index_with_start_course_code(self) -> None:
        args = make_args(row_index=3, start_course_code="CS1010", row_count=5)

        with self.assertRaisesRegex(SystemExit, "--row-index cannot be used"):
            course.validate_args(args)

    def test_validate_args_rejects_row_count_without_start_course_code(self) -> None:
        args = make_args(row_count=5)

        with self.assertRaisesRegex(SystemExit, "--row-count requires --start-course-code"):
            course.validate_args(args)

    def test_validate_args_rejects_non_positive_row_count(self) -> None:
        args = make_args(start_course_code="CS1010", row_count=0)

        with self.assertRaisesRegex(SystemExit, "--row-count must be a positive integer"):
            course.validate_args(args)

    def test_validate_args_rejects_in_place_with_start_course_code(self) -> None:
        args = make_args(start_course_code="CS1010", row_count=5, in_place=True)

        with self.assertRaisesRegex(SystemExit, "--in-place cannot be used"):
            course.validate_args(args)

    def test_resolve_load_and_output_paths_uses_existing_skillsfuture_file(self) -> None:
        temp_path = Path("tmp_path_resolution")
        input_path = temp_path / "modules.csv"
        output_path = temp_path / "modules_skillsfuture.csv"

        with mock.patch.object(Path, "exists", autospec=True) as exists_mock:
            exists_mock.side_effect = lambda self: self == output_path
            load_path, resolved_output_path = course.resolve_load_and_output_paths(
                input_path,
                make_args(start_course_code="CS1010", row_count=5),
            )

        self.assertEqual(load_path, output_path)
        self.assertEqual(resolved_output_path, output_path)

    def test_resolve_load_and_output_paths_bootstraps_from_input_when_output_missing(self) -> None:
        temp_path = Path("tmp_path_resolution")
        input_path = temp_path / "modules.csv"

        with mock.patch.object(Path, "exists", autospec=True, return_value=False):
            load_path, output_path = course.resolve_load_and_output_paths(
                input_path,
                make_args(start_course_code="CS1010", row_count=5),
            )

        self.assertEqual(load_path, input_path)
        self.assertEqual(output_path, temp_path / "modules_skillsfuture.csv")

    def test_resolve_load_and_output_paths_honors_explicit_output_file(self) -> None:
        temp_path = Path("tmp_path_resolution")
        input_path = temp_path / "modules.csv"
        explicit_output = temp_path / "custom.csv"

        with mock.patch.object(Path, "exists", autospec=True) as exists_mock:
            exists_mock.side_effect = lambda self: self == explicit_output
            load_path, output_path = course.resolve_load_and_output_paths(
                input_path,
                make_args(
                    start_course_code="CS1010",
                    row_count=5,
                    output_file=str(explicit_output),
                ),
            )

        self.assertEqual(load_path, explicit_output)
        self.assertEqual(output_path, explicit_output)

    def test_resolve_batch_row_window_finds_exact_course_code(self) -> None:
        df = pd.DataFrame(
            [
                {"moduleCode": "ACC1701", "description": "A"},
                {"moduleCode": "CS1010", "description": "B"},
                {"moduleCode": "CS1010E", "description": "C"},
            ]
        )

        start_row, end_row = course.resolve_batch_row_window(
            df,
            make_args(start_course_code="CS1010", row_count=1),
        )

        self.assertEqual(start_row, 1)
        self.assertEqual(end_row, 2)

    def test_resolve_batch_row_window_caps_at_end_of_file(self) -> None:
        df = pd.DataFrame(
            [
                {"moduleCode": "ACC1701", "description": "A"},
                {"moduleCode": "CS1010", "description": "B"},
                {"moduleCode": "CS2030", "description": "C"},
            ]
        )

        start_row, end_row = course.resolve_batch_row_window(
            df,
            make_args(start_course_code="CS1010", row_count=10),
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


if __name__ == "__main__":
    unittest.main()
