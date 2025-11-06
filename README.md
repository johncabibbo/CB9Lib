# CB9Lib - Cloud Box 9 Python Library

**Version 1.3.0** - A comprehensive utility library for Cloud Box 9 projects

A powerful, feature-rich Python library providing terminal colors, interactive UI components, advanced logging, file operations, input validation, testing framework, and common helper functions for building professional CLI applications.

## ✨ Features

### Core Features
- **🎨 Terminal Colors & Themes**: Full ANSI color support with predefined themes
- **🖥️ Interactive UI**: Menus, selection lists, progress bars, confirmations
- **📊 Table Formatting**: Beautiful table output for data display
- **📝 Advanced Logging**: Multi-level logging with file and console output
- **⚙️ Command-Line Parsing**: Enhanced argument parsing with CB9 styling
- **✅ Input Validation**: Validators for emails, IPs, numbers, paths, and more
- **📁 File Utilities**: Advanced file operations (copy, move, search)
- **🧪 Testing Framework**: Built-in assertions and test utilities
- **🔧 Helper Functions**: JSON config, timestamps, and utility functions
- **🌐 Cross-Platform**: Works on macOS, Linux, and Windows

---

## 📦 Installation

### From Source (Development)

```bash
# Clone or navigate to the repository
cd CB9Lib

# Install in development mode
pip install -e .
```

### From Git

```bash
pip install git+https://github.com/yourusername/CB9Lib.git
```

### From PyPI (when published)

```bash
pip install CB9Lib
```

---

## 🚀 Quick Start Guide

### 1. Terminal Colors & Themes

```python
from CB9Lib import color_text, RED, GREEN, YELLOW, CYAN, BOLD

# Basic colored text
print(color_text("Error!", fg=RED, style=BOLD))
print(color_text("Success!", fg=GREEN))
print(color_text("Warning!", fg=YELLOW))

# Apply color themes
from CB9Lib import apply_theme, get_theme_color

apply_theme('ocean')
primary = get_theme_color('primary')
print(color_text("Ocean theme text", fg=primary))

# Available themes: 'default', 'ocean', 'forest', 'sunset', 'mono'
```

### 2. Interactive UI Components

```python
from CB9Lib import menu, select_list, progress_bar, confirm
import time

# Interactive menu
choice = menu(
    "Main Menu",
    ["View Dashboard", "Edit Settings", "Run Report", "Exit"]
)

# Selection list (single or multi-select)
languages = ["Python", "JavaScript", "Go", "Rust"]
selected = select_list("Choose languages", languages, multi=True)

# Progress bar
for i in range(100):
    progress_bar(i, 100, label="Processing", show_percent=True)
    time.sleep(0.02)

# Confirmation dialog
if confirm("Continue with operation?", default=True):
    print("Continuing...")
```

### 3. Table Formatting

```python
from CB9Lib import print_table, print_dict_table

# Basic table
headers = ["Name", "Age", "City"]
rows = [
    ["Alice", "28", "San Francisco"],
    ["Bob", "35", "New York"],
    ["Charlie", "42", "Chicago"]
]
print_table(headers, rows, align=['left', 'right', 'left'])

# Dictionary table
data = [
    {"server": "web-01", "cpu": "45%", "status": "OK"},
    {"server": "web-02", "cpu": "78%", "status": "WARNING"},
    {"server": "db-01", "cpu": "23%", "status": "OK"}
]
print_dict_table(data)
```

### 4. Advanced Logging

```python
from CB9Lib import get_logger, INFO, WARNING, ERROR

# Create a logger
logger = get_logger("MyApp", level=INFO, filename="app.log")

# Log at different levels
logger.debug("Detailed debug information")
logger.info("Application started")
logger.warning("Low disk space")
logger.error("Failed to connect to database")
logger.critical("System failure!")

# Logs appear in console (colored) and file (timestamped)
```

### 5. Command-Line Parsing

```python
from CB9Lib import CB9ArgParser

# Create parser
parser = CB9ArgParser(
    name="backup_tool",
    version="1.0",
    description="Backup utility with options"
)

# Add arguments
parser.add_argument("source", help="Source directory")
parser.add_argument("destination", help="Destination directory")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
parser.add_argument("--format", "-f", default="zip", help="Archive format")

# Parse arguments
args = parser.parse()
print(f"Source: {args.source}")
print(f"Verbose: {args.verbose}")
```

### 6. Input Validation

```python
from CB9Lib import (
    is_valid_email, is_valid_ip, is_valid_hostname,
    is_valid_number, is_valid_integer, is_valid_port
)

# Validate email
if is_valid_email("user@example.com"):
    print("Valid email!")

# Validate IP address
if is_valid_ip("192.168.1.1"):
    print("Valid IP!")

# Validate hostname
if is_valid_hostname("example.com"):
    print("Valid hostname!")

# Validate numbers
if is_valid_integer("42"):
    print("Valid integer!")

if is_valid_number("3.14159"):
    print("Valid number!")

# Validate port
if is_valid_port(8080):
    print("Valid port!")
```

### 7. File Utilities

```python
from CB9Lib import copy_file, move_file, search_files, get_file_info

# Copy a file
copy_file("/path/to/source.txt", "/path/to/dest.txt", overwrite=True)

# Move a file
move_file("/path/to/file.txt", "/path/to/new_location.txt")

# Search for files
txt_files = search_files("/path/to/dir", "*.txt", recursive=True)
print(f"Found {len(txt_files)} text files")

# Get file information
info = get_file_info("/path/to/file.txt")
print(f"Size: {info['size_mb']} MB")
print(f"Modified: {info['modified']}")
```

### 8. Testing Framework

```python
from CB9Lib import (
    assert_equals, assert_true, assert_false,
    test_suite, get_test_stats
)

# Basic assertions
assert_equals(2 + 2, 4, "Addition test")
assert_true(10 > 5, "Comparison test")
assert_false("" == "test", "Empty string test")

# Define test functions
def test_math():
    """Test mathematical operations."""
    assert_equals(5 * 5, 25, "Multiplication")
    assert_true(100 > 50, "Greater than")

def test_strings():
    """Test string operations."""
    assert_equals(len("test"), 4, "String length")
    assert_true("hello" in "hello world", "Substring")

# Run test suite
test_suite([test_math, test_strings])

# Get statistics
stats = get_test_stats()
print(f"Tests run: {stats['total']}, Passed: {stats['passed']}")
```

### 9. Headers & UI Components

```python
from CB9Lib import header, footerMenu, clear_screen, pause

# Display application header
header("My Application", "v2.0", subtitle="Data Processor")

# Clear the screen
clear_screen()

# Display footer menu and get input
choice = footerMenu("Press [Q] to quit, [H] for help")

# Pause for user
pause("Press Enter to continue...")
```

---

## 📚 Complete Example Application

```python
#!/usr/bin/env python3
"""
Example CLI application using CB9Lib v1.3
"""
import sys
from pathlib import Path

# Add CB9Lib to path
sys.path.insert(0, str(Path(__file__).parent / "CB9Lib"))

from CB9Lib import (
    # UI Components
    header, clear_screen, menu, confirm, progress_bar,
    # Colors
    color_text, GREEN, CYAN, RED, YELLOW, BOLD,
    # Logging
    get_logger, INFO,
    # Tables
    print_table,
    # Validation
    is_valid_email
)

def main():
    """Main application entry point."""

    # Initialize logger
    logger = get_logger("MyApp", level=INFO, filename="myapp.log")
    logger.info("Application started")

    while True:
        # Display header
        header("Data Manager", "v1.0", subtitle="Process & Analyze")

        # Show menu
        choice = menu(
            "Main Menu",
            [
                "View Data",
                "Process Files",
                "Generate Report",
                "Settings"
            ],
            allow_quit=True
        )

        if choice == 'quit':
            if confirm("Are you sure you want to exit?", default=False):
                break
            continue

        clear_screen()

        # Process choice
        if choice == '1':
            # Display data table
            header("Data View", "v1.0")
            headers = ["ID", "Name", "Status", "Progress"]
            rows = [
                ["001", "Task Alpha", "Running", "75%"],
                ["002", "Task Beta", "Complete", "100%"],
                ["003", "Task Gamma", "Pending", "0%"]
            ]
            print_table(headers, rows, align=['left', 'left', 'center', 'right'])
            input("\nPress Enter to continue...")

        elif choice == '2':
            # Process files with progress
            header("File Processor", "v1.0")
            print(color_text("Processing files...\n", CYAN))

            import time
            for i in range(101):
                progress_bar(i, 100, label="Progress", show_percent=True)
                time.sleep(0.02)

            print(color_text("\n✓ Processing complete!", GREEN, style=BOLD))
            logger.info("File processing completed")
            input("\nPress Enter to continue...")

        elif choice == '3':
            # Generate report
            header("Report Generator", "v1.0")
            print(color_text("Report generated successfully!", GREEN))
            logger.info("Report generated")
            input("\nPress Enter to continue...")

        elif choice == '4':
            # Settings
            header("Settings", "v1.0")
            print("Settings menu coming soon...")
            input("\nPress Enter to continue...")

        clear_screen()

    # Exit
    clear_screen()
    print(color_text("Thank you for using Data Manager!", CYAN, style=BOLD))
    logger.info("Application exited")
    print()

if __name__ == "__main__":
    main()
```

---

## 📖 API Reference

For complete API documentation, see:
- **[API_REFERENCE.md](API_REFERENCE.md)** - Detailed markdown documentation
- **[API_REFERENCE.html](API_REFERENCE.html)** - HTML version with navigation

### Quick Module Reference

#### `colors.py` - Colors, Styles & Themes
- Color constants: `RED`, `GREEN`, `BLUE`, `CYAN`, `YELLOW`, `MAGENTA`, etc.
- Bright colors: `BRIGHT_RED`, `BRIGHT_GREEN`, etc.
- Styles: `BOLD`, `DIM`, `ITALIC`, `UNDERLINE`
- Functions: `color_text()`, `banner()`, `test_colors()`
- Themes: `apply_theme()`, `get_theme_color()`, `list_themes()`

#### `func.py` - Core Utilities
- UI: `header()`, `footerMenu()`, `clear_screen()`, `pause()`, `sleep()`
- Interactive: `menu()`, `select_list()`, `progress_bar()`, `confirm()`
- Tables: `print_table()`, `table_format()`, `print_dict_table()`
- JSON: `load_json_config()`, `save_json_config()`
- Files: `copy_file()`, `move_file()`, `search_files()`, `get_file_info()`
- Logging: `Logger`, `get_logger()`, `write_log()`, `log_header()`, `log_footer()`

#### `globals.py` - Global Settings
- Paths: `ROOT_DIR`, `LOG_DIR`, `TEMP_DIR`
- Functions: `get_timestamp()`, `print_banner()`

#### `args.py` - Command-Line Parsing
- Classes: `CB9ArgParser`
- Functions: `parse_simple_args()`, `get_script_name()`, `get_all_args()`

#### `validators.py` - Input Validation
- Functions: `is_valid_email()`, `is_valid_ip()`, `is_valid_hostname()`
- `is_valid_number()`, `is_valid_integer()`, `is_valid_port()`
- `is_valid_path()`, `validate_input()`, `validate_choice()`

#### `testing.py` - Testing Framework
- Assertions: `assert_equals()`, `assert_true()`, `assert_false()`
- Suite: `test_suite()`, `get_test_stats()`, `reset_test_stats()`
- Utilities: `mock_input()`, `capture_output()`

#### `imgvid.py` - Image/Video Utilities
- Functions: `create_thumb_resize()`, `list_thumbnails()`

---

## 🎯 Demo & Examples

Run the interactive demo to see all features in action:

```bash
cd CB9Lib
./demo_all_features.py
```

The demo includes:
1. Interactive UI demonstrations
2. Table formatting examples
3. Advanced logging with log levels
4. Command-line parsing
5. Input validation tests
6. File utilities demonstrations
7. Color themes showcase
8. Testing framework examples

---

## 📋 Requirements

- Python >= 3.10
- No external dependencies (uses only Python standard library)

---

## 🔄 Version History

### v1.3.0 (2025-10-25)
**Major Feature Release**
- ✨ Added interactive UI functions (`menu`, `select_list`, `progress_bar`, `confirm`)
- 📊 Added table formatting (`print_table`, `table_format`, `print_dict_table`)
- 📝 Added advanced logging (`Logger` class, log levels, file logging)
- ⚙️ Added command-line parsing module (`CB9ArgParser`, `parse_simple_args`)
- ✅ Added input validation module (email, IP, hostname, number validators)
- 🧪 Added testing framework (`assert_*`, `test_suite`, test statistics)
- 🎨 Added color themes (`THEME_*`, `apply_theme`, `get_theme_color`)
- 📁 Added advanced file utilities (`copy_file`, `move_file`, `search_files`, `get_file_info`)

### v1.2.0 (2025-10-23)
- Added `logRotate()` function for log file rotation
- Enhanced function documentation with parameter descriptions
- Added return type annotations

### v1.1.0 (2025-10-22)
- Initial release as installable package
- Full ANSI color support with TTY detection
- UI components for CLI applications
- File and JSON utilities
- Basic logging functionality

---

## ⚠️ Backward Compatibility

**CB9Lib v1.3 is fully backward compatible** with v1.1 and v1.2. All existing scripts will continue to work without modifications. The new features are additive and don't change existing function signatures.

If you're upgrading from v1.1 or v1.2:
- ✅ No code changes required
- ✅ All existing imports work
- ✅ All existing functions unchanged
- ✨ New features available for use when needed

---

## 📝 License

Copyright © 2025 Cloud Box 9 Inc. All rights reserved.

---

## 👥 Maintainer

Cloud Box 9 Inc.

---

## 🤝 Support

For issues, questions, or contributions, please contact Cloud Box 9 Inc.

---

## 🔗 Additional Resources

- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [API Reference](API_REFERENCE.md) - Complete function documentation
- [Changelog](CHANGELOG_v1.3.md) - Detailed version history
- [Demo Script](demo_all_features.py) - Interactive feature demonstration
