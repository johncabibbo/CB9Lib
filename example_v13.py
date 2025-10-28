#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
"""
CB9Lib v1.3 Feature Demonstration
Showcases all new features added in version 1.3
"""

from CB9Lib import *
import time

def demo_interactive_ui():
    """Demonstrate interactive UI features"""
    header("Interactive UI Demo", "v1.3", "Menus, Selection, Progress")

    # Menu demo
    print(color_text("\n1. Menu Demo", fg=BRIGHT_CYAN, style=BOLD))
    choice = menu("Main Menu", [
        "Process Data",
        "View Reports",
        "Settings"
    ])
    print(f"You selected: {choice}\n")

    # Multi-select demo
    print(color_text("2. Multi-Select Demo", fg=BRIGHT_CYAN, style=BOLD))
    databases = ["mysql_prod", "mysql_dev", "postgres_app"]
    selected = select_list("Select databases to backup:", databases, multi=True)
    print(f"Selected: {selected}\n")

    # Progress bar demo
    print(color_text("3. Progress Bar Demo", fg=BRIGHT_CYAN, style=BOLD))
    for i in range(1, 51):
        progress_bar(i, 50, label="Processing", width=40)
        time.sleep(0.02)

    # Confirm demo
    print(color_text("\n4. Confirmation Demo", fg=BRIGHT_CYAN, style=BOLD))
    if confirm("Continue to next demo?", default=True):
        print(color_text("Continuing...\n", fg=GREEN))

    pause()


def demo_tables():
    """Demonstrate table formatting"""
    header("Table Formatting Demo", "v1.3", "Display Data in Tables")

    # Basic table
    print(color_text("\n1. Basic Table", fg=BRIGHT_CYAN, style=BOLD))
    headers = ["Snapshot ID", "Size", "Status", "Date"]
    rows = [
        ["snap-001", "8.5 GB", "✓ Complete", "2024-10-20"],
        ["snap-002", "8.7 GB", "✓ Complete", "2024-10-21"],
        ["snap-003", "8.3 GB", "⚠ Partial", "2024-10-22"]
    ]
    print_table(headers, rows, align=['left', 'right', 'center', 'left'])

    # Dictionary table
    print(color_text("\n2. Dictionary Table", fg=BRIGHT_CYAN, style=BOLD))
    backups = [
        {"name": "mysql_prod", "size": "2.4 GB", "status": "OK"},
        {"name": "postgres_app", "size": "1.8 GB", "status": "OK"},
        {"name": "redis_cache", "size": "512 MB", "status": "OK"}
    ]
    print_dict_table(backups)

    pause()


def demo_advanced_logging():
    """Demonstrate advanced logging system"""
    header("Advanced Logging Demo", "v1.3", "Log Levels & Filtering")

    print(color_text("\n1. Creating Logger with INFO level", fg=BRIGHT_CYAN, style=BOLD))
    log = get_logger("DemoApp", level=INFO, filename="demo_app.log")

    log.debug("This won't show (below INFO level)")
    log.info("Application started")
    log.warning("Low disk space: 10% remaining")
    log.error("Failed to connect to database")
    log.critical("System shutdown initiated")

    print(color_text("\n2. Changing Log Level to DEBUG", fg=BRIGHT_CYAN, style=BOLD))
    log.set_level(DEBUG)
    log.debug("Now debug messages will appear")
    log.info("Debug logging enabled")

    print(color_text("\n3. Old-style logging still works!", fg=BRIGHT_CYAN, style=BOLD))
    log_file = log_header("OldStyleJob", "v1.0")
    write_log("Processing 100 files", log_file)
    write_log("Complete", log_file)
    log_footer("OldStyleJob", "v1.0", log_file)

    pause()


def demo_color_themes():
    """Demonstrate color themes"""
    header("Color Themes Demo", "v1.3", "Predefined Color Schemes")

    themes = [
        ("DEFAULT", THEME_DEFAULT),
        ("OCEAN", THEME_OCEAN),
        ("FOREST", THEME_FOREST),
        ("SUNSET", THEME_SUNSET),
        ("MONO", THEME_MONO)
    ]

    for name, theme in themes:
        apply_theme(theme)
        print(f"\n{color_text(name + ' Theme:', fg=get_theme_color('primary'), style=BOLD)}")
        print(f"  Primary:   {color_text('Sample Text', fg=get_theme_color('primary'))}")
        print(f"  Secondary: {color_text('Sample Text', fg=get_theme_color('secondary'))}")
        print(f"  Success:   {color_text('Sample Text', fg=get_theme_color('success'))}")
        print(f"  Warning:   {color_text('Sample Text', fg=get_theme_color('warning'))}")
        print(f"  Error:     {color_text('Sample Text', fg=get_theme_color('error'))}")

    # Reset to default
    apply_theme(THEME_DEFAULT)

    pause()


def demo_file_utilities():
    """Demonstrate advanced file utilities"""
    header("File Utilities Demo", "v1.3", "Copy, Move, Search")

    print(color_text("\n1. Search for Python files", fg=BRIGHT_CYAN, style=BOLD))
    results = search_files("/Users/john-ash/Documents/script/CB9Lib", "*.py", recursive=False)
    print(f"Found {len(results)} Python files:")
    for f in results[:5]:  # Show first 5
        print(f"  - {f}")

    print(color_text("\n2. Get file info", fg=BRIGHT_CYAN, style=BOLD))
    info = get_file_info(__file__)
    if info:
        print(f"  Name:     {info['name']}")
        print(f"  Size:     {info['size_mb']} MB")
        print(f"  Modified: {info['modified']}")

    pause()


def demo_validation():
    """Demonstrate input validation"""
    header("Input Validation Demo", "v1.3", "Email, Number, Path")

    print(color_text("\n1. Validation Functions", fg=BRIGHT_CYAN, style=BOLD))

    # Email validation
    emails = ["user@example.com", "invalid.email"]
    for email in emails:
        valid = is_valid_email(email)
        status = color_text("✓ Valid", fg=GREEN) if valid else color_text("✗ Invalid", fg=RED)
        print(f"  {email}: {status}")

    # Number validation
    print("\n" + color_text("2. Number Range Validation", fg=BRIGHT_CYAN, style=BOLD))
    numbers = ["42", "150", "abc"]
    for num in numbers:
        valid = is_valid_number(num, min_val=0, max_val=100)
        status = color_text("✓ Valid", fg=GREEN) if valid else color_text("✗ Invalid", fg=RED)
        print(f"  {num} (0-100): {status}")

    # Path validation
    print("\n" + color_text("3. Path Validation", fg=BRIGHT_CYAN, style=BOLD))
    paths = [__file__, "/nonexistent/path"]
    for path in paths:
        valid = is_valid_path(path, must_exist=True)
        status = color_text("✓ Exists", fg=GREEN) if valid else color_text("✗ Not Found", fg=RED)
        print(f"  {path}: {status}")

    pause()


def demo_testing():
    """Demonstrate testing framework"""
    header("Testing Framework Demo", "v1.3", "Unit Test Utilities")

    with test_suite("Math Operations"):
        assert_equals(2 + 2, 4, "Addition test")
        assert_equals(5 * 5, 25, "Multiplication test")
        assert_true(10 > 5, "Greater than test")
        assert_false(3 > 10, "Less than test")
        assert_equals(len([1, 2, 3]), 3, "List length test")


def main():
    """Main demo menu"""
    while True:
        header("CB9Lib v1.3 Feature Demo", "v1.3.0", "All New Features")

        choice = menu("Select a demo:", [
            "1. Interactive UI (Menu, Select, Progress)",
            "2. Table Formatting",
            "3. Advanced Logging",
            "4. Color Themes",
            "5. File Utilities",
            "6. Input Validation",
            "7. Testing Framework",
            "8. Run All Demos"
        ], allow_back=False)

        if choice == 'quit':
            print(color_text("\nGoodbye!\n", fg=BRIGHT_CYAN))
            break
        elif choice == '1':
            demo_interactive_ui()
        elif choice == '2':
            demo_tables()
        elif choice == '3':
            demo_advanced_logging()
        elif choice == '4':
            demo_color_themes()
        elif choice == '5':
            demo_file_utilities()
        elif choice == '6':
            demo_validation()
        elif choice == '7':
            demo_testing()
        elif choice == '8':
            demo_interactive_ui()
            demo_tables()
            demo_advanced_logging()
            demo_color_themes()
            demo_file_utilities()
            demo_validation()
            demo_testing()
            print(color_text("\n✓ All demos complete!\n", fg=BRIGHT_GREEN, style=BOLD))
            pause()


if __name__ == "__main__":
    main()
