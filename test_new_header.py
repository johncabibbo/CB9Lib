#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
# =============================================================================
# Filename: test_new_header.py
# Project: CB9Lib
# Version: 1.0
# Last Modified Date: 2025-10-22
# Category: Testing
# OS: Mac/Linux/Windows
# Maintainer: Cloud Box 9
# -----------------------------------------------------------------------------
# Description:
#   Test script demonstrating the new Cloud Box 9 header format.
#
#   Features:
#     • Uses updated header format with = borders
#     • Includes Category and OS fields
#     • Shows proper formatting for CB9 projects
#
# Usage:
#   python3 test_new_header.py
#
# Notes:
#   • This is a demonstration file
#   • Header format is now saved in .claude/preferences.md
# -----------------------------------------------------------------------------
# Revision History:
#   v1.0 — 2025-10-22 — Initial creation to demonstrate new header format
# =============================================================================

from CB9Lib import *

def main():
    header("New Header Format Test", "v1.0")
    print(color_text("This file demonstrates the new Cloud Box 9 header format!", fg=GREEN, style=BOLD))
    print()
    print(color_text("Key features of the new format:", fg=CYAN))
    print(color_text("  • Equal signs (=) for top/bottom borders", fg=YELLOW))
    print(color_text("  • Category field for organization", fg=YELLOW))
    print(color_text("  • OS compatibility field", fg=YELLOW))
    print(color_text("  • Detailed Description with Features section", fg=YELLOW))
    print(color_text("  • Usage examples", fg=YELLOW))
    print(color_text("  • Notes section for important details", fg=YELLOW))
    print(color_text("  • Revision History with em-dash separator", fg=YELLOW))

if __name__ == "__main__":
    main()
