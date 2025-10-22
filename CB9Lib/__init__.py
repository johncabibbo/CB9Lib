#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: __init__.py
# Project: CB9Lib Library
# Version: 1.0
# Maintainer: Cloud Box 9 Inc
# Last Modified Date: 2025-10-22
# -----------------------------------------------------------------------------
# Description:
#   Initializes the CB9Lib package namespace and imports core modules.
# -----------------------------------------------------------------------------

# Import modules
from . import globals
from . import colors
from . import func

# Import commonly used items for convenience
from .colors import (
    color_text, banner, enable_colors, test_colors,
    RED, GREEN, YELLOW, BLUE, CYAN, MAGENTA, WHITE, BLACK,
    BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE,
    BRIGHT_CYAN, BRIGHT_MAGENTA, BRIGHT_WHITE, BRIGHT_BLACK,
    BOLD, DIM, ITALIC, UNDERLINE, RESET
)

from .func import (
    clear_screen, pause, sleep,
    load_json_config, save_json_config,
    header, footerMenu,
    file_exists, folder_exists, ensure_folder, list_files,
    write_log, log_header, log_footer, test_ui
)

from .globals import (
    ROOT_DIR, LOG_DIR, TEMP_DIR,
    get_timestamp, print_banner, SETTINGS
)

__version__ = "1.1.0"

__all__ = [
    # Modules
    "globals", "colors", "func",
    # Color functions
    "color_text", "banner", "enable_colors", "test_colors",
    # Colors
    "RED", "GREEN", "YELLOW", "BLUE", "CYAN", "MAGENTA", "WHITE", "BLACK",
    "BRIGHT_RED", "BRIGHT_GREEN", "BRIGHT_YELLOW", "BRIGHT_BLUE",
    "BRIGHT_CYAN", "BRIGHT_MAGENTA", "BRIGHT_WHITE", "BRIGHT_BLACK",
    "BOLD", "DIM", "ITALIC", "UNDERLINE", "RESET",
    # Utility functions
    "clear_screen", "pause", "sleep",
    "load_json_config", "save_json_config",
    "header", "footerMenu",
    "file_exists", "folder_exists", "ensure_folder", "list_files",
    "write_log", "log_header", "log_footer", "test_ui",
    # Global settings
    "ROOT_DIR", "LOG_DIR", "TEMP_DIR",
    "get_timestamp", "print_banner", "SETTINGS",
]
