#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: func.py
# Project: Shared Library
# Version: 1.2
# Description: Common functions for Cloud Box 9 projects (UI + JSON + Console).
# Maintainer: Cloud Box 9 Inc.
# Last Modified Date: 2025-10-23
# -----------------------------------------------------------------------------
# Function List:
# -----------------------------------------------------------------------------
# clear_screen()
#     Clear the terminal screen
#
# pause(msg: str = "Press Enter to continue...")
#     Pause for user input with custom message
#     msg: Message to display to user
#
# sleep(seconds: float = 1.0)
#     Wait for N seconds with visual indicator
#     seconds: Number of seconds to wait
#
# load_json_config(jsonFileName: str) -> dict
#     Load and parse JSON config file, returns empty dict on error
#     jsonFileName: Path to JSON file (absolute or relative)
#                   Example: "config.json" or "/Users/user/config.json"
#
# save_json_config(jsonFileName: str, data: dict)
#     Save dictionary to JSON file with indentation
#     jsonFileName: Path to JSON file (absolute or relative)
#                   Example: "config.json" or "/Users/user/config.json"
#     data: Dictionary to save as JSON
#
# header(title: str = "Untitled Script", version: str = "v1.2", subtitle: str = "", width: int = 0)
#     Display full header banner with title, version, and optional subtitle
#     title: Title of the script/application
#     version: Version string (e.g., "v1.2")
#     subtitle: Optional subtitle text
#     width: Terminal width (0 = auto-detect)
#
# footerMenu(legend: str = "", width: int = 0) -> str
#     Display footer menu with legend and prompt, returns user input
#     legend: Menu legend/instructions to display
#     width: Terminal width (0 = auto-detect)
#
# file_exists(path: str) -> bool
#     Check if a file exists
#     path: Path to file (absolute or relative)
#           Example: "data.txt" or "/Users/user/data.txt"
#
# folder_exists(path: str) -> bool
#     Check if a directory exists
#     path: Path to directory (absolute or relative)
#           Example: "logs" or "/Users/user/Documents/logs"
#
# ensure_folder(path: str)
#     Create directory if not existing
#     path: Path to directory (absolute or relative)
#           Example: "output" or "/Users/user/Documents/output"
#
# list_files(path: str, ext: str = None) -> list
#     List files in directory, optionally filter by extension
#     path: Directory path (absolute or relative)
#           Example: "data" or "/Users/user/Documents/data"
#     ext: Optional file extension filter (e.g., ".py", ".json")
#
# write_log(message: str, filename: str = None)
#     Write log message to file and print to console
#     message: Log message to write
#     filename: Optional log file path (absolute or relative, auto-generated if None)
#               Example: "/Users/user/Documents/logs/app.log"
#
# log_header(job_name: str, version: str = "v1.2", filename: str = None) -> str
#     Write log header at start of job, returns filename
#     job_name: Name of the job/script
#     version: Version string
#     filename: Optional log file path (absolute or relative, auto-generated if None)
#               Example: "/Users/user/Documents/logs/backup.log"
#
# log_footer(job_name: str, version: str = "v1.2", filename: str = None)
#     Write log footer at end of job
#     job_name: Name of the job/script
#     version: Version string
#     filename: Log file path (absolute or relative)
#               Example: "/Users/user/Documents/logs/backup.log"
#
# logRotate(script_name: str, version: str = "v1.2", old_filename: str = None) -> str
#     Rotate log file, create new timestamped file with header, returns new filename
#     script_name: Name of the script/job
#     version: Version string
#     old_filename: Optional previous log file to close (absolute or relative)
#                   Example: "/Users/user/Documents/logs/backup_2025-10-23.log"
#
# test_ui()
#     Demonstrate header, footer, and color usage
#
# -----------------------------------------------------------------------------
# Revision History:
# -----------------------------------------------------------------------------
# v1.2 (2025-10-23)
#   • Added logRotate() function for log file rotation with timestamps
#   • Enhanced Function List with complete parameter descriptions
#   • Added return type annotations to function signatures
#   • Added detailed argument descriptions for each parameter
#   • Added path type specifications and example inputs for file/folder arguments
#
# v1.1 (2025-10-22)
#   • Added full Function List header and Revision History section.
#   • Integrated write_log() logging function below File Utilities.
#   • Confirmed Cloud Box 9 formatting, UI header/footer consistency.
#   • Version officially marked as baseline v1.1.
# -----------------------------------------------------------------------------

import os, json, shutil, time
from datetime import datetime
from CB9Lib.colors import *
from CB9Lib.globals import *

# -----------------------------------------------------------------------------
# Global Vars
# -----------------------------------------------------------------------------
width = shutil.get_terminal_size().columns

# -----------------------------------------------------------------------------
# Core Utilities
# -----------------------------------------------------------------------------
def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")


def pause(msg: str = "Press Enter to continue..."):
    """Pause for user input."""
    input(f"{DIM}{msg}{RESET}")


def sleep(seconds: float = 1.0):
    """Wait for N seconds (with small visual indicator)."""
    print(f"{DIM}Please wait{RESET}", end="", flush=True)
    for _ in range(int(seconds * 2)):
        time.sleep(0.5)
        print(f"{DIM}.{RESET}", end="", flush=True)
    print()

# -----------------------------------------------------------------------------
# JSON Helpers
# -----------------------------------------------------------------------------
def load_json_config(jsonFileName: str) -> dict:
    """
    Load and parse JSON config file.
    Returns empty dict if file missing or invalid.
    """
    try:
        with open(jsonFileName, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(color_text(f"[ERROR] Config file not found: {jsonFileName}", RED, style=BOLD))
    except json.JSONDecodeError as e:
        print(color_text(f"[ERROR] Invalid JSON format: {e}", RED, style=BOLD))
    return {}


def save_json_config(jsonFileName: str, data: dict):
    """
    Save dictionary to JSON file with indentation.
    """
    try:
        with open(jsonFileName, "w") as f:
            json.dump(data, f, indent=4)
        print(color_text(f"[OK] Saved: {jsonFileName}", GREEN))
    except Exception as e:
        print(color_text(f"[ERROR] Could not save JSON: {e}", RED))

# -----------------------------------------------------------------------------
# UI Elements
# -----------------------------------------------------------------------------
def header(title: str = "Untitled Script", version: str = "v1.2", subtitle: str = "", width: int = 0):
    """
    Display a full header banner with title and version.
    """
    if width == 0:
        width = shutil.get_terminal_size().columns
    if subtitle != "":
        subtitle = "["+subtitle+"]"
    clear_screen()
    print("-" * width)
    print(f" {BOLD}{CYAN}{title}{MAGENTA} {version} {BRIGHT_GREEN}{subtitle}{RESET}")
    print("-" * width)


def footerMenu(legend: str = "", width: int = 0) -> str:
    """
    Display footer menu with legend and prompt for user input.
    Returns the choice entered by the user.
    """
    if width == 0:
        width = shutil.get_terminal_size().columns
    print("-" * width)
    if legend:
        print(color_text(legend, fg=BRIGHT_YELLOW))
    print("-" * width)
    choice = input(f"{BOLD}{WHITE}> {RESET}").strip().lower()
    return choice

# -----------------------------------------------------------------------------
# File Utilities
# -----------------------------------------------------------------------------
def file_exists(path: str) -> bool:
    """Check if a file exists."""
    return os.path.isfile(path)


def folder_exists(path: str) -> bool:
    """Check if a directory exists."""
    return os.path.isdir(path)


def ensure_folder(path: str):
    """Create directory if not existing."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(color_text(f"[Created] {path}", GREEN))
    else:
        print(color_text(f"[Exists]  {path}", CYAN))


def list_files(path: str, ext: str = None) -> list:
    """List files in a directory (optionally filter by extension)."""
    try:
        files = [f for f in os.listdir(path) if not ext or f.endswith(ext)]
        return sorted(files)
    except Exception as e:
        print(color_text(f"[ERROR] {e}", RED))
        return []

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
def write_log(message: str, filename: str = None):
    """Write a log message to file and print it to console."""
    ensure_folder(LOG_DIR)
    if not filename:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(LOG_DIR, f"script_{timestamp}.log")

    try:
        with open(filename, "a") as log_file:
            log_file.write(f"[{datetime.now()}] {message}\n")
        print(f"{BOLD}{YELLOW}{message}{RESET}")
    except Exception as e:
        print(color_text(f"[ERROR] Could not write log: {e}", RED, style=BOLD))


def log_header(job_name: str, version: str = "v1.2", filename: str = None):
    """
    Write a log header at the start of a job.
    Logs the job name, version, and start timestamp with a separator line.
    """
    ensure_folder(LOG_DIR)
    if not filename:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(LOG_DIR, f"{job_name.replace(' ', '_')}_{timestamp}.log")

    separator = "-" * 80
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filename, "a") as log_file:
            log_file.write(f"{separator}\n")
            log_file.write(f"JOB: {job_name} {version}\n")
            log_file.write(f"START: {start_time}\n")
            log_file.write(f"{separator}\n")
        print(color_text(f"[LOG] Started: {job_name} {version}", BRIGHT_GREEN, style=BOLD))
        return filename
    except Exception as e:
        print(color_text(f"[ERROR] Could not write log header: {e}", RED, style=BOLD))
        return None


def log_footer(job_name: str, version: str = "v1.2", filename: str = None):
    """
    Write a log footer at the end of a job.
    Logs the job name, version, and end timestamp.
    """
    if not filename:
        print(color_text("[WARNING] No log filename provided for footer", YELLOW))
        return

    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    separator = "-" * 80

    try:
        with open(filename, "a") as log_file:
            log_file.write(f"END: {end_time}\n")
            log_file.write(f"JOB: {job_name} {version}\n")
            log_file.write(f"{separator}\n\n")
        print(color_text(f"[LOG] Completed: {job_name} {version}", BRIGHT_GREEN, style=BOLD))
    except Exception as e:
        print(color_text(f"[ERROR] Could not write log footer: {e}", RED, style=BOLD))


def logRotate(script_name: str, version: str = "v1.2", old_filename: str = None) -> str:
    """
    Rotate the log file and create a new one with a header.

    Creates a new timestamped log file with a header containing:
    - Created Date
    - Script Name
    - Version

    Args:
        script_name: Name of the script/job
        version: Version string (default "v1.2")
        old_filename: Optional previous log file (for reference only)

    Returns:
        str: Path to the new log file
    """
    ensure_folder(LOG_DIR)

    # Close old log with footer if provided
    if old_filename:
        try:
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            separator = "-" * 80
            with open(old_filename, "a") as log_file:
                log_file.write(f"END: {end_time}\n")
                log_file.write(f"LOG ROTATED\n")
                log_file.write(f"{separator}\n\n")
        except Exception as e:
            print(color_text(f"[WARNING] Could not close old log: {e}", YELLOW))

    # Create new log file with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_filename = os.path.join(LOG_DIR, f"{script_name.replace(' ', '_')}_{timestamp}.log")

    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    separator = "-" * 80

    try:
        with open(new_filename, "w") as log_file:
            log_file.write(f"{separator}\n")
            log_file.write(f"LOG FILE CREATED: {created_date}\n")
            log_file.write(f"SCRIPT: {script_name}\n")
            log_file.write(f"VERSION: {version}\n")
            log_file.write(f"{separator}\n")
        print(color_text(f"[LOG] Rotated: {new_filename}", BRIGHT_CYAN, style=BOLD))
        return new_filename
    except Exception as e:
        print(color_text(f"[ERROR] Could not create rotated log: {e}", RED, style=BOLD))
        return None

# -----------------------------------------------------------------------------
# Debug/Test
# -----------------------------------------------------------------------------
def test_ui():
    """Demonstrate header, footer, and color usage."""
    header("Demo Script", "v3.9")
    print(color_text("This is a demo of the Cloud Box 9 shared library.", BRIGHT_CYAN))
    choice = footerMenu("Use arrow keys or shortcuts to navigate.")
    print(color_text(f"You selected: {choice}", YELLOW))