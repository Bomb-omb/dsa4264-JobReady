import os
import time
import glob
import shutil
import csv
import keyboard
import platform
import pandas as pd
import pyautogui
import pyperclip

system = platform.system()

if system == "Darwin":
    CMD_KEY = "command"
elif system == "Windows":
    CMD_KEY = "ctrl"
else:
    CMD_KEY = "ctrl"

print(f"Running on: {system}")


pyautogui.FAILSAFE = True

# =========================
# CONFIG
# =========================
INPUT_FILE = "data/2025-2026_module_clean_with_prereq.csv"
PROGRESS_FILE = "unique_progress.csv"
FINAL_FILE = "modules_with_skills.csv"
DOWNLOAD_DIR = os.path.expanduser("~/Downloads")

# Replace these with your actual coordinates
TEXTBOX_POS = (3372, 923)
DOWNLOAD_BTN_POS = (3928, 1004)
RESET_BTN_POS = (3567, 1448)

WAIT_AFTER_PASTE = 2
WAIT_AFTER_RESET = 2
DOWNLOAD_TIMEOUT = 5
MAX_RETRIES = 1
ERROR_REFRESH_THRESHOLD = 5
TIME_FOR_REFRESH = 2
error_count = 0

# =========================
# HELPERS
# =========================

def manual_pause():
    print("\n⏸️  PAUSED — Refresh website now")
    print("▶️  Press 'r' to resume...")

    keyboard.wait("r")

    print("✅ Resuming script...\n")
    time.sleep(1)

def get_latest_csv(after_time: float):
    files = glob.glob(os.path.join(DOWNLOAD_DIR, "*.csv"))
    if not files:
        return None

    newest = max(files, key=os.path.getmtime)
    if os.path.getmtime(newest) > after_time:
        return newest
    return None


def wait_for_download(after_time: float, timeout: int = DOWNLOAD_TIMEOUT):
    start = time.time()
    while time.time() - start < timeout:
        file = get_latest_csv(after_time)
        if file:
            time.sleep(1.0)  # let the download finish writing
            return file
        time.sleep(0.5)
    return None

def refresh_website():
    print("\n🔄 Auto-refreshing website...")

    system = platform.system()

    if system == "Darwin":   # Mac
        pyautogui.hotkey(CMD_KEY, "r")

    elif system == "Windows":   # Windows
        pyautogui.hotkey("ctrl", "r")

    else:
        print(f"⚠️ Unsupported OS: {system}")
        return

    # Wait for full reload
    time.sleep(TIME_FOR_REFRESH)

    print(f"✅ Website refreshed on {system}.")

def extract_skills_from_csv(file_path: str) -> str:
    skills = []
    record_skills = False

    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, skipinitialspace=True)

        for row in reader:
            for cell in row:

                cleaned = str(cell).strip()

                if not cleaned:
                    continue

                if cleaned == "input_text":
                    continue

                if cleaned == "extracted_skills":
                    record_skills = True
                    continue

                if record_skills:
                    skill_name = cleaned.split("; Tags:")[0].strip()
                    skills.append(skill_name)

    # remove duplicates but keep order
    skills = list(dict.fromkeys(skills))

    return " | ".join(skills)


def paste_text(text: str):

    # Double-click to activate textbox
    pyautogui.click(TEXTBOX_POS, clicks=3)

    time.sleep(0.5)

    # Triple-click to fully select existing text
    pyautogui.hotkey(CMD_KEY, "a")

    time.sleep(0.3)

    pyautogui.press("backspace")

    time.sleep(0.3)

    pyperclip.copy(text)
    pyautogui.hotkey(CMD_KEY, "v")

    time.sleep(WAIT_AFTER_PASTE)

    pyautogui.click(RESET_BTN_POS)

    time.sleep(0.5)


def click_download_and_read() -> str | None:
    download_start = time.time()
    time.sleep(5)
    pyautogui.click(DOWNLOAD_BTN_POS)

    downloaded_file = wait_for_download(download_start, timeout=DOWNLOAD_TIMEOUT)
    if downloaded_file is None:
        return None

    try:
        skills = extract_skills_from_csv(downloaded_file)
    finally:
        # delete the downloaded file regardless of success/failure
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)

    return skills


def reset_page():
    pyautogui.click(RESET_BTN_POS)
    time.sleep(WAIT_AFTER_RESET)


# =========================
# LOAD DATA
# =========================
df = pd.read_csv(INPUT_FILE)

# Keep original row order, but deduplicate on description
unique_df = df[["moduleCode", "description"]].drop_duplicates().copy()
unique_df["skills"] = ""
unique_df["status"] = "pending"
unique_df["skills"] = unique_df["skills"].astype("object")
unique_df["status"] = unique_df["status"].astype("object")

# If progress file exists, resume from it
if os.path.exists(PROGRESS_FILE):
    saved = pd.read_csv(PROGRESS_FILE)
    if set(["description", "skills", "status"]).issubset(saved.columns):
        unique_df = saved.copy()

unique_df["skills"] = unique_df["skills"].fillna("").astype("object")
unique_df["status"] = unique_df["status"].fillna("pending").astype("object")

print(f"Original rows: {len(df)}")
print(f"Unique descriptions to process: {len(unique_df)}")

print("Starting in 3 seconds. Keep browser fixed and do not touch mouse/keyboard.")
time.sleep(3)

# =========================
# MAIN LOOP
# =========================
for i, row in unique_df.iterrows():
    if str(row["status"]).lower() == "success":
        continue

    print(f"Processing {row['moduleCode']}")

    description = str(row["description"])
    print(f"Processing unique row {i+1}/{len(unique_df)}")

    success = False
    last_error = ""

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"  Attempt {attempt}/{MAX_RETRIES}")

            paste_text(description)

            skills = click_download_and_read()

            if not skills:
                raise RuntimeError("No skills extracted or download failed.")

            unique_df.at[i, "skills"] = skills
            unique_df.at[i, "status"] = "success"
            success = True

            error_count = 0 

            print(f"  Success: {skills}")
            reset_page()
            break

        except Exception as e:
            last_error = str(e)
            unique_df.at[i, "status"] = f"error: {last_error}"
            error_count += 1

            print(f"  Error: {last_error}")
            print(f"  Current error count: {error_count}")

            # Auto refresh if too many errors
            if error_count >= ERROR_REFRESH_THRESHOLD:

                print("⚠️ Too many errors — refreshing website")

                # Save progress first
                unique_df.to_csv(PROGRESS_FILE, index=False)

                refresh_website()

                # Reset counter
                error_count = 0

                # Reset UI after refresh
                try:
                    reset_page()
                except Exception:
                    pass

            # normal retry reset
            try:
                reset_page()
            except Exception:
                pass

            time.sleep(1.5)

    if not success:
        print(f"  Failed after retries: {last_error}")

    # save progress after every row
    unique_df.to_csv(PROGRESS_FILE, index=False)

# =========================
# MAP BACK TO FULL DATASET
# =========================
final_df = df.merge(
    unique_df[["description", "skills", "status"]],
    on="description",
    how="left"
)

final_df.to_csv(FINAL_FILE, index=False)

print(f"Done. Progress saved to: {PROGRESS_FILE}")
print(f"Final output saved to: {FINAL_FILE}")