#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: test_logRotate.py
# Project: CB9Lib Library
# Version: 1.0
# Description: Test script for the new logRotate function
# Last Modified Date: 2025-10-23
# -----------------------------------------------------------------------------

from CB9Lib import *

def main():
    header("Test logRotate", "v1.0")

    print(color_text("Testing logRotate function...", BRIGHT_CYAN, style=BOLD))
    print()

    # Test 1: Create initial log
    print(color_text("Test 1: Creating initial log file", YELLOW))
    log1 = log_header("TestScript", "v1.0")
    write_log("This is the first log entry", log1)
    write_log("This is the second log entry", log1)
    print(color_text(f"Created: {log1}", GREEN))
    print()

    # Test 2: Rotate log
    print(color_text("Test 2: Rotating to new log file", YELLOW))
    sleep(1)  # Wait 1 second to ensure different timestamp
    log2 = logRotate("TestScript", "v1.0", log1)
    write_log("This is the first entry in the new log", log2)
    write_log("This is the second entry in the new log", log2)
    print(color_text(f"Rotated to: {log2}", GREEN))
    print()

    # Test 3: Rotate again
    print(color_text("Test 3: Rotating again", YELLOW))
    sleep(1)  # Wait 1 second to ensure different timestamp
    log3 = logRotate("TestScript", "v1.0", log2)
    write_log("Third log file - first entry", log3)
    print(color_text(f"Rotated to: {log3}", GREEN))
    print()

    # Close final log
    log_footer("TestScript", "v1.0", log3)

    print()
    print(color_text("=" * 60, CYAN))
    print(color_text("Test completed! Check ~/Documents/logs/ for log files:", BRIGHT_GREEN, style=BOLD))
    print(color_text(f"  - {log1}", WHITE))
    print(color_text(f"  - {log2}", WHITE))
    print(color_text(f"  - {log3}", WHITE))
    print(color_text("=" * 60, CYAN))

    pause()

if __name__ == "__main__":
    main()
