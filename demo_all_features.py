#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: demo_all_features.py
# Project: CB9Lib Demonstration
# Version: 1.0
# Description: Comprehensive demonstration of all CB9Lib v1.3 features
# Maintainer: Cloud Box 9 Inc.
# Last Modified Date: 2025-11-06
# -----------------------------------------------------------------------------

import os
import sys
import time
from pathlib import Path

# Add CB9Lib to path
sys.path.insert(0, str(Path(__file__).parent))

from CB9Lib import (
    # Core utilities
    header, footerMenu, clear_screen, pause, sleep,
    # Interactive UI (Feature 1)
    menu, select_list, progress_bar, confirm,
    # Table formatting (Feature 2)
    print_table, table_format, print_dict_table,
    # Advanced logging (Feature 3)
    Logger, get_logger, DEBUG, INFO, WARNING, ERROR, CRITICAL,
    # Command-line parsing (Feature 4)
    parse_simple_args, CB9ArgParser, get_script_name, get_all_args,
    # Input validation (Feature 5)
    is_valid_email, is_valid_number, is_valid_integer, is_valid_path,
    is_valid_ip, is_valid_hostname, is_valid_port,
    validate_input, validate_choice,
    # File utilities (Feature 6)
    copy_file, move_file, search_files, get_file_info,
    file_exists, folder_exists, ensure_folder,
    # Color themes (Feature 7)
    THEME_DEFAULT, THEME_OCEAN, THEME_FOREST, THEME_SUNSET, THEME_MONO,
    apply_theme, get_theme_color, get_current_theme, list_themes,
    # Testing framework (Feature 8)
    assert_equals, assert_true, assert_false,
    test_suite, get_test_stats, reset_test_stats,
    # Colors
    color_text, CYAN, GREEN, YELLOW, RED, BLUE, MAGENTA,
    BOLD, DIM, RESET,
    BRIGHT_CYAN, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_RED
)

# Demo configuration
TEMP_DIR = Path(__file__).parent / "temp_demo"


def demo_interactive_ui():
    """Feature 1: Interactive UI demonstrations."""
    header("Feature 1: Interactive UI", "v1.3")

    print(color_text("This feature includes menus, selection lists, progress bars, and confirmations.\n", CYAN))

    # Demo 1: Menu
    print(color_text("Demo 1a: Simple Menu", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    choice = menu(
        "Select an option",
        ["View Dashboard", "Edit Settings", "Run Report", "Export Data"],
        allow_back=False,
        allow_quit=False
    )
    print(color_text(f"✓ You selected option: {choice}\n", GREEN))

    # Demo 2: Confirm dialog
    print(color_text("Demo 1b: Confirmation Dialog", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    response = confirm("Do you want to continue with the demo?", default=True)
    print(color_text(f"✓ Your response: {'Yes' if response else 'No'}\n", GREEN))

    if not response:
        return

    # Demo 3: Select list (single)
    print(color_text("Demo 1c: Single Selection List", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    items = ["Python", "JavaScript", "Go", "Rust", "Java"]
    selected = select_list("Choose your favorite programming language", items, multi=False)
    if selected:
        print(color_text(f"✓ You selected: {selected[0]}\n", GREEN))

    # Demo 4: Progress bar
    print(color_text("Demo 1d: Progress Bar", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    total = 50
    for i in range(total + 1):
        progress_bar(i, total, width=40, label="Processing", show_percent=True)
        time.sleep(0.02)
    print(color_text("✓ Progress complete!\n", GREEN))

    pause("\nPress Enter to continue to next feature...")


def demo_table_formatting():
    """Feature 2: Table formatting demonstrations."""
    header("Feature 2: Table Formatting", "v1.3")

    print(color_text("This feature includes formatted tables and dict tables.\n", CYAN))

    # Demo 1: Basic table
    print(color_text("Demo 2a: Basic Table with Headers", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    headers = ["Name", "Age", "City", "Status"]
    rows = [
        ["Alice Smith", "28", "San Francisco", "Active"],
        ["Bob Jones", "35", "New York", "Active"],
        ["Charlie Brown", "42", "Chicago", "Inactive"],
        ["Diana Prince", "31", "Los Angeles", "Active"]
    ]
    print_table(headers, rows, align=['left', 'right', 'left', 'center'], border=True)

    # Demo 2: Dictionary table
    print(color_text("\nDemo 2b: Dictionary Table", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    dict_data = [
        {"name": "Server-01", "cpu": "45%", "memory": "78%", "status": "OK"},
        {"name": "Server-02", "cpu": "23%", "memory": "56%", "status": "OK"},
        {"name": "Server-03", "cpu": "89%", "memory": "92%", "status": "WARNING"},
        {"name": "Server-04", "cpu": "12%", "memory": "34%", "status": "OK"}
    ]
    print_dict_table(dict_data)

    # Demo 3: Table format (string output)
    print(color_text("\nDemo 2c: Table Format (String Output)", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    table_str = table_format(["Task", "Duration", "Result"],
                            [["Build", "2m 34s", "Success"],
                             ["Test", "1m 12s", "Success"],
                             ["Deploy", "45s", "Success"]])
    print(color_text("Table as string (useful for logging):", YELLOW))
    print(table_str)

    pause("\nPress Enter to continue to next feature...")


def demo_advanced_logging():
    """Feature 3: Advanced logging demonstrations."""
    header("Feature 3: Advanced Logging", "v1.3")

    print(color_text("This feature includes log levels, filtering, and file logging.\n", CYAN))

    # Demo 1: Basic logger
    print(color_text("Demo 3a: Logger with Different Levels", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    logger = get_logger("DemoApp", level=DEBUG)

    logger.debug("This is a debug message - detailed diagnostic info")
    logger.info("This is an info message - general information")
    logger.warning("This is a warning message - something to watch")
    logger.error("This is an error message - something went wrong")
    logger.critical("This is a critical message - system failure!")

    # Demo 2: Log level filtering
    print(color_text("\nDemo 3b: Log Level Filtering (WARNING and above only)", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    logger2 = Logger("FilteredApp", level=WARNING, console=True, colored=True)
    logger2.debug("You won't see this (level too low)")
    logger2.info("You won't see this either (level too low)")
    logger2.warning("But you'll see this warning!")
    logger2.error("And this error!")

    # Demo 3: File logging
    print(color_text("\nDemo 3c: File Logging", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    ensure_folder(TEMP_DIR)
    log_file = TEMP_DIR / "demo.log"

    file_logger = Logger("FileApp", level=INFO, filename=str(log_file), console=True)
    file_logger.info("This message is written to both console and file")
    file_logger.warning("Log file location: " + str(log_file))

    if log_file.exists():
        print(color_text(f"✓ Log file created: {log_file}", GREEN))

    pause("\nPress Enter to continue to next feature...")


def demo_command_line_parsing():
    """Feature 4: Command-line parsing demonstrations."""
    header("Feature 4: Command-Line Parsing", "v1.3")

    print(color_text("This feature includes argument parsing utilities.\n", CYAN))

    # Demo 1: Get script name
    print(color_text("Demo 4a: Script Information", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    print(f"Script name: {color_text(get_script_name(), YELLOW)}")
    print(f"All arguments: {color_text(str(get_all_args()), YELLOW)}")

    # Demo 2: Simple args parsing
    print(color_text("\nDemo 4b: Simple Arguments Example", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)
    print("Example: python script.py --verbose --output=file.txt input.csv")
    print(color_text("Would be parsed as:", CYAN))

    # Simulate command-line args
    example_args = ["--verbose", "--output=file.txt", "input.csv"]
    print(f"  Flags: --verbose")
    print(f"  Options: --output=file.txt")
    print(f"  Positional: input.csv")

    # Demo 3: CB9ArgParser
    print(color_text("\nDemo 4c: CB9ArgParser (Advanced)", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    parser = CB9ArgParser(
        name="backup_tool",
        version="1.0",
        description="Backup utility with various options"
    )

    parser.add_argument("source", help="Source directory to backup")
    parser.add_argument("destination", help="Destination for backup")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--compress", "-c", action="store_true", help="Compress backup files")
    parser.add_argument("--format", "-f", default="zip", help="Archive format (zip, tar, tar.gz)")

    print(color_text("Parser configured with:", YELLOW))
    print("  • 2 positional arguments (source, destination)")
    print("  • 2 boolean flags (--verbose, --compress)")
    print("  • 1 option with default (--format=zip)")
    print(color_text("\n✓ Use parser.parse() to parse sys.argv", GREEN))
    print(color_text("  Example: backup_tool /src /dst --verbose --format=tar.gz", DIM))

    pause("\nPress Enter to continue to next feature...")


def demo_input_validation():
    """Feature 5: Input validation demonstrations."""
    header("Feature 5: Input Validation", "v1.3")

    print(color_text("This feature includes validators for common input types.\n", CYAN))

    # Demo 1: Email validation
    print(color_text("Demo 5a: Email Validation", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    test_emails = ["user@example.com", "invalid.email", "test@domain.co.uk", "@nodomain.com"]
    for email in test_emails:
        result = is_valid_email(email)
        status = color_text("✓ Valid", GREEN) if result else color_text("✗ Invalid", RED)
        print(f"  {email:<25} {status}")

    # Demo 2: Number validation
    print(color_text("\nDemo 5b: Number Validation", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    test_numbers = ["42", "3.14159", "-17", "abc", "12.34.56"]
    for num in test_numbers:
        is_int = is_valid_integer(num)
        is_num = is_valid_number(num)
        int_status = "Integer" if is_int else "-"
        num_status = "Number" if is_num else "-"
        print(f"  {num:<15} {int_status:<10} {num_status}")

    # Demo 3: IP address validation
    print(color_text("\nDemo 5c: IP Address Validation", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    test_ips = ["192.168.1.1", "256.1.1.1", "10.0.0.1", "not.an.ip", "8.8.8.8"]
    for ip in test_ips:
        result = is_valid_ip(ip)
        status = color_text("✓ Valid", GREEN) if result else color_text("✗ Invalid", RED)
        print(f"  {ip:<20} {status}")

    # Demo 4: Hostname validation
    print(color_text("\nDemo 5d: Hostname Validation", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    test_hosts = ["example.com", "sub.domain.co.uk", "-invalid", "valid-host", "test_host"]
    for host in test_hosts:
        result = is_valid_hostname(host)
        status = color_text("✓ Valid", GREEN) if result else color_text("✗ Invalid", RED)
        print(f"  {host:<25} {status}")

    # Demo 5: Port validation
    print(color_text("\nDemo 5e: Port Validation", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    test_ports = [80, 443, 8080, 0, 65535, 99999, -1]
    for port in test_ports:
        result = is_valid_port(port)
        status = color_text("✓ Valid", GREEN) if result else color_text("✗ Invalid", RED)
        print(f"  Port {port:<10} {status}")

    pause("\nPress Enter to continue to next feature...")


def demo_file_utilities():
    """Feature 6: File utilities demonstrations."""
    header("Feature 6: File Utilities", "v1.3")

    print(color_text("This feature includes advanced file operations.\n", CYAN))

    ensure_folder(TEMP_DIR)

    # Demo 1: Create test files
    print(color_text("Demo 6a: Creating Test Files", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    test_file1 = TEMP_DIR / "test1.txt"
    test_file2 = TEMP_DIR / "test2.txt"

    test_file1.write_text("This is test file 1")
    print(color_text(f"✓ Created: {test_file1}", GREEN))

    # Demo 2: Copy file
    print(color_text("\nDemo 6b: Copy File", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    dest_file = TEMP_DIR / "test1_copy.txt"
    copy_file(str(test_file1), str(dest_file), overwrite=True)

    # Demo 3: Get file info
    print(color_text("\nDemo 6c: Get File Information", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    info = get_file_info(str(test_file1))
    if info:
        print(f"  Name: {info['name']}")
        print(f"  Size: {info['size_bytes']} bytes")
        print(f"  Modified: {info['modified']}")
        print(f"  Extension: {info['extension']}")

    # Demo 4: Search files
    print(color_text("\nDemo 6d: Search Files", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    found = search_files(str(TEMP_DIR), "*.txt", recursive=False)
    print(color_text(f"Found {len(found)} .txt files:", YELLOW))
    for f in found:
        print(f"  • {Path(f).name}")

    # Demo 5: Move file
    print(color_text("\nDemo 6e: Move File", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    moved_file = TEMP_DIR / "moved.txt"
    move_file(str(dest_file), str(moved_file))

    pause("\nPress Enter to continue to next feature...")


def demo_color_themes():
    """Feature 7: Color themes demonstrations."""
    header("Feature 7: Color Themes", "v1.3")

    print(color_text("This feature includes predefined color schemes.\n", CYAN))

    # Demo 1: List themes
    print(color_text("Demo 7a: Available Themes", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    themes = list_themes()
    print(color_text("Available themes:", YELLOW))
    for theme in themes:
        print(f"  • {theme}")

    # Demo 2: Apply different themes
    print(color_text("\nDemo 7b: Theme Examples", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    sample_text = "This is how text looks in this theme"

    for theme_name in ['default', 'ocean', 'forest', 'sunset']:
        apply_theme(theme_name)
        primary = get_theme_color('primary')
        secondary = get_theme_color('secondary')
        accent = get_theme_color('accent')

        print(f"\n{BOLD}{theme_name.upper()} Theme:{RESET}")
        print(f"  Primary:   {color_text(sample_text, primary)}")
        print(f"  Secondary: {color_text(sample_text, secondary)}")
        print(f"  Accent:    {color_text(sample_text, accent)}")

    # Restore default theme
    apply_theme('default')

    pause("\nPress Enter to continue to next feature...")


def demo_testing_framework():
    """Feature 8: Testing framework demonstrations."""
    header("Feature 8: Testing Framework", "v1.3")

    print(color_text("This feature includes test assertions and utilities.\n", CYAN))

    # Demo 1: Basic assertions
    print(color_text("Demo 8a: Assertions", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    reset_test_stats()

    print("Running test assertions...")
    assert_equals(2 + 2, 4, "Addition test")
    assert_equals("hello".upper(), "HELLO", "String test")
    assert_true(10 > 5, "Comparison test")
    assert_false("" == "test", "Empty string test")

    # This will fail on purpose to show failure reporting
    assert_equals(10, 11, "Intentional failure test")

    # Demo 2: Test statistics
    print(color_text("\nDemo 8b: Test Statistics", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    stats = get_test_stats()
    print(f"  Total tests: {stats['total']}")
    passed_msg = f"Passed: {stats['passed']}"
    failed_msg = f"Failed: {stats['failed']}"
    print(f"  {color_text(passed_msg, GREEN)}")
    print(f"  {color_text(failed_msg, RED)}")

    # Demo 3: Test suite
    print(color_text("\nDemo 8c: Test Suite Example", BRIGHT_CYAN, style=BOLD))
    print("-" * 60)

    def sample_test_1():
        """Test basic math operations."""
        assert_equals(5 * 5, 25, "Multiplication")
        assert_true(100 > 50, "Greater than")

    def sample_test_2():
        """Test string operations."""
        assert_equals(len("test"), 4, "String length")
        assert_true("hello" in "hello world", "Substring check")

    print("Running test suite with 2 test functions...")
    test_suite([sample_test_1, sample_test_2])

    final_stats = get_test_stats()
    print(color_text(f"\n✓ Test suite complete: {final_stats['passed']}/{final_stats['total']} passed", GREEN))

    pause("\nPress Enter to finish demo...")


def cleanup_demo():
    """Clean up temporary demo files."""
    import shutil
    if TEMP_DIR.exists():
        try:
            shutil.rmtree(TEMP_DIR)
            print(color_text(f"\n✓ Cleaned up temp directory: {TEMP_DIR}", GREEN))
        except Exception as e:
            print(color_text(f"\n⚠ Could not clean up: {e}", YELLOW))


def main():
    """Main demo menu."""

    while True:
        header("CB9Lib v1.3 Feature Demonstration", "v1.0")

        print(color_text("This demo showcases all 8 major features of CB9Lib v1.3\n", CYAN))

        choice = menu(
            "Select a feature to demonstrate",
            [
                "Interactive UI (menus, progress bars, confirmations)",
                "Table Formatting (print tables, dict tables)",
                "Advanced Logging (log levels, filtering, file logging)",
                "Command-Line Parsing (argument handling)",
                "Input Validation (email, IP, hostname, numbers)",
                "File Utilities (copy, move, search, file info)",
                "Color Themes (predefined color schemes)",
                "Testing Framework (assertions, test suites)",
                "Run All Demos"
            ],
            allow_back=False,
            allow_quit=True
        )

        if choice == 'quit':
            break

        clear_screen()

        if choice == '1':
            demo_interactive_ui()
        elif choice == '2':
            demo_table_formatting()
        elif choice == '3':
            demo_advanced_logging()
        elif choice == '4':
            demo_command_line_parsing()
        elif choice == '5':
            demo_input_validation()
        elif choice == '6':
            demo_file_utilities()
        elif choice == '7':
            demo_color_themes()
        elif choice == '8':
            demo_testing_framework()
        elif choice == '9':
            # Run all demos in sequence
            demo_interactive_ui()
            demo_table_formatting()
            demo_advanced_logging()
            demo_command_line_parsing()
            demo_input_validation()
            demo_file_utilities()
            demo_color_themes()
            demo_testing_framework()

        clear_screen()

    # Clean up and exit
    cleanup_demo()

    clear_screen()
    print("=" * 80)
    print(f"{BOLD}{CYAN}CB9Lib Feature Demo {YELLOW}v1.0{RESET}")
    print("=" * 80)
    print(f"{CYAN}Demo exiting...{RESET}\n")
    print(f"{YELLOW}Copyright © 2025 Cloud Box 9 Inc. All rights reserved.{RESET}\n")


if __name__ == "__main__":
    main()
