from pathlib import Path
import pandas as pd

skills_taxo_path = Path("data/skills_taxo.csv")
mapping_path = Path("data/raw/jobsandskills-skillsfuture-tsc-to-unique-skills-mapping.xlsx")
output_path = Path("data/acc/skills_taxo_acc.csv")

target_sectors = ["Accountancy", "Financial Services"]

skills_taxo = pd.read_csv(skills_taxo_path, encoding="utf-8-sig")

sector_mapping = pd.read_excel(
    mapping_path,
    sheet_name="TSC to Unique Skill Mapping",
    usecols=["sector_title", "parent_skill_title"],
)

filtered_titles = (
    sector_mapping.loc[
        sector_mapping["sector_title"].isin(target_sectors),
        "parent_skill_title",
    ]
    .dropna()
    .astype(str)
    .str.strip()
    .drop_duplicates()
)

skills_taxo_acc = (
    skills_taxo.loc[
        skills_taxo["parent_skill_title"].astype(str).str.strip().isin(filtered_titles)
    ]
    .drop_duplicates()
    .sort_values("parent_skill_title")
    .reset_index(drop=True)
)

output_path.parent.mkdir(parents=True, exist_ok=True)
skills_taxo_acc.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Saved {len(skills_taxo_acc)} rows to {output_path}")
skills_taxo_acc.head()
