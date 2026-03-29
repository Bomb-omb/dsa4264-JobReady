import argparse
import unittest
from pathlib import Path

import pandas as pd

import extract_skillsfuture_course as course


def make_args() -> argparse.Namespace:
    return argparse.Namespace(
        id_column="moduleCode",
        text_column="description",
        output_column="extracted_skills",
        apps_tools_column="extracted_apps_tools",
        status_column="done",
    )


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


if __name__ == "__main__":
    unittest.main()
