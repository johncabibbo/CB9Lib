#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: func.py
# Project: Shared Library
# Version: 1.1
# Description: Common functions for Cloud Box 9 projects (UI + JSON + Console).
# Maintainer: Cloud Box 9 Inc.
# Last Modified Date: 2025-10-22
# -----------------------------------------------------------------------------
# Function List:
# -----------------------------------------------------------------------------
# clear_screen()
# pause(msg: str = "Press Enter to continue...")
# sleep(seconds: float = 1.0)
# load_json_config(jsonFileName: str)
# save_json_config(jsonFileName: str, data: dict)
# header(title: str = "Untitled Script", version: str = "v1.0")
# footerMenu(legend: str = "")
# file_exists(path: str)
# folder_exists(path: str)
# ensure_folder(path: str)
# list_files(path: str, ext: str = None)
# write_log(message: str, filename: str = None)
# test_ui()
# -----------------------------------------------------------------------------
# Revision History:
# -----------------------------------------------------------------------------
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
def header(title: str = "Untitled Script", version: str = "v1.0", subtitle: str = "", width: int = 0):
    """
    Display a full header banner with title and version.
    """
    if width == 0:
        width = shutil.get_terminal_size().columns
    if subtitle != "":
        subtitle = "["+subtitle+"]"
    clear_screen()
    print("-" * width)
    print(f"  {BOLD}{CYAN}{title}{MAGENTA} {version} {BRIGHT_GREEN}{subtitle}{RESET}")
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

# -----------------------------------------------------------------------------
# Debug/Test
# -----------------------------------------------------------------------------
def test_ui():
    """Demonstrate header, footer, and color usage."""
    header("Demo Script", "v3.9")
    print(color_text("This is a demo of the Cloud Box 9 shared library.", BRIGHT_CYAN))
    choice = footerMenu("Use arrow keys or shortcuts to navigate.")
    print(color_text(f"You selected: {choice}", YELLOW))