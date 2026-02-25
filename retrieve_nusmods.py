import requests
import json
import os

def get_module_list(acad_year):
    url = f"https://api.nusmods.com/v2/{acad_year}/moduleList.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for academic year {acad_year}. Status code: {response.status_code}")

def get_module_info(acad_year):
    url = f"https://api.nusmods.com/v2/{acad_year}/moduleInfo.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch module info for academic year {acad_year}. Status code: {response.status_code}")

# Save to JSON files
def save_to_json(acad_year):
    folder_name = os.path.join("data", "raw", "nusmods")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    module_list = get_module_list(acad_year)
    module_info = get_module_info(acad_year)

    if module_list is not None:
        with open(os.path.join(folder_name, f"{acad_year}_moduleList.json"), "w") as f:
            json.dump(module_list, f, indent=4)
    
    if module_info is not None:
        with open(os.path.join(folder_name, f"{acad_year}_moduleInfo.json"), "w") as f:
            json.dump(module_info, f, indent=4)

    print(f"Data for academic year {acad_year} saved successfully.")

if __name__ == "__main__":
    acad_year = ["2022-2023", "2023-2024", "2024-2025", "2025-2026"]
    for year in acad_year:
        save_to_json(year)
    