# CB9Lib v1.3.0 Changelog

**Release Date:** 2025-10-25
**Backward Compatibility:** ✅ **100% Compatible** - All existing scripts will continue to work without modifications

---

## 🎯 Summary

CB9Lib v1.3.0 adds **8 major feature categories** with **50+ new functions** while maintaining complete backward compatibility. All existing scripts using CB9Lib v1.2 will continue to work without any changes.

---

## ✨ New Features

### 1. **Interactive UI Components** (`func.py`)
Enhanced user interaction with menus, selections, and progress indicators.

**New Functions:**
- `menu(title, options, allow_back=True, allow_quit=True)` - Interactive numbered menu
- `select_list(title, items, multi=False, selected=None)` - Single/multi-select lists
- `progress_bar(current, total, width=50, label="", show_percent=True)` - Visual progress indicator
- `confirm(prompt, default=True)` - Yes/no confirmation dialog

**Example:**
```python
from CB9Lib import menu, select_list, progress_bar, confirm

choice = menu("Main Menu", ["Backup", "Restore", "Settings"])
databases = select_list("Select databases:", ["mysql", "postgres"], multi=True)
for i in range(100):
    progress_bar(i+1, 100, label="Processing")
if confirm("Continue?"):
    print("Continuing...")
```

---

### 2. **Table Formatting** (`func.py`)
Display data in formatted, bordered tables.

**New Functions:**
- `print_table(headers, rows, align=None, border=True)` - Print formatted table
- `table_format(headers, rows, align=None)` - Return table as string (for logging)
- `print_dict_table(dict_list, keys=None)` - Print table from list of dictionaries

**Example:**
```python
from CB9Lib import print_table, print_dict_table

headers = ["Name", "Size", "Status"]
rows = [
    ["backup1.tar", "1.2 GB", "Complete"],
    ["backup2.tar", "980 MB", "Complete"]
]
print_table(headers, rows, align=['left', 'right', 'center'])

# Or from dictionaries
backups = [
    {"name": "mysql", "size": "2.4 GB", "status": "OK"},
    {"name": "postgres", "size": "1.8 GB", "status": "OK"}
]
print_dict_table(backups)
```

---

### 3. **Advanced Logging System** (`func.py`)
Log levels, filtering, and colored console output - works alongside existing logging.

**New Features:**
- `Logger` class with level-based filtering
- `get_logger(name, level=INFO, filename=None)` - Create logger instance
- Log level constants: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
- Methods: `logger.debug()`, `logger.info()`, `logger.warning()`, `logger.error()`, `logger.critical()`
- `logger.set_level(level)` - Dynamic level adjustment

**Backward Compatible:** Old logging functions (`write_log`, `log_header`, `log_footer`) still work perfectly!

**Example:**
```python
from CB9Lib import get_logger, INFO, DEBUG, WARNING

# NEW logging system
log = get_logger("MyApp", level=INFO, filename="app.log")
log.debug("This won't show")  # Below INFO level
log.info("Application started")
log.warning("Low disk space")
log.error("Connection failed")
log.set_level(DEBUG)  # Now debug messages will appear

# OLD logging still works!
log_file = log_header("MyJob", "v1.0")
write_log("Processing...", log_file)
log_footer("MyJob", "v1.0", log_file)
```

---

### 4. **Command-Line Parsing** (New module: `args.py`)
Parse command-line arguments with ease.

**New Functions:**
- `parse_simple_args(expected_args=None)` - Simple argument parser
- `CB9ArgParser(name, version, description="")` - Enhanced argparse wrapper
- `get_script_name()` - Get running script name
- `get_all_args()` - Get all command-line arguments

**Example:**
```python
from CB9Lib.args import CB9ArgParser, parse_simple_args

# Simple parsing
args = parse_simple_args(['database', 'output'])
# Returns: {'database': 'db1', 'output': '/backups', 'dry_run': True}

# Advanced parsing
parser = CB9ArgParser("Backup Tool", "v2.0")
parser.add_argument('database', help='Database name')
parser.add_argument('--dry-run', action='store_true')
args = parser.parse()
```

---

### 5. **Input Validation** (New module: `validators.py`)
Validate user input with built-in validators.

**New Functions:**
- `is_valid_email(email)` - Email format validation
- `is_valid_number(value, min_val=None, max_val=None)` - Number range validation
- `is_valid_integer(value, min_val=None, max_val=None)` - Integer validation
- `is_valid_path(path, must_exist=False, must_be_file=False, must_be_dir=False)` - Path validation
- `is_valid_ip(ip, version=4)` - IPv4/IPv6 validation
- `is_valid_hostname(hostname)` - Hostname validation
- `is_valid_port(port)` - Port number validation (1-65535)
- `validate_input(prompt, validator, error_msg="", max_attempts=3)` - Interactive validation
- `validate_choice(prompt, valid_choices, case_sensitive=False)` - Choice validation

**Example:**
```python
from CB9Lib.validators import *

# Validation checks
if is_valid_email("user@example.com"):
    print("Valid email")

if is_valid_number("42", min_val=0, max_val=100):
    print("Valid number in range")

# Interactive validation
email = validate_input(
    "Enter email:",
    is_valid_email,
    "Invalid email format"
)

env = validate_choice("Environment:", ["dev", "staging", "prod"])
```

---

### 6. **Advanced File Utilities** (`func.py`)
Enhanced file operations beyond basic existence checks.

**New Functions:**
- `copy_file(src, dst, overwrite=False)` - Safe file copy
- `move_file(src, dst)` - Safe file move
- `search_files(path, pattern, recursive=True)` - Search with glob patterns
- `get_file_info(path)` - Get detailed file information (size, dates, etc.)

**Backward Compatible:** Old functions (`file_exists`, `folder_exists`, `ensure_folder`, `list_files`, `remove_files`) unchanged!

**Example:**
```python
from CB9Lib import copy_file, move_file, search_files, get_file_info

# Copy file
copy_file("/source/backup.tar", "/dest/backup.tar", overwrite=True)

# Search for files
python_files = search_files("/project", "*.py", recursive=True)
print(f"Found {len(python_files)} Python files")

# Get file details
info = get_file_info("backup.tar")
print(f"Size: {info['size_mb']} MB, Modified: {info['modified']}")
```

---

### 7. **Color Themes** (`colors.py`)
Predefined color schemes for consistent styling.

**New Features:**
- Theme dictionaries: `THEME_DEFAULT`, `THEME_OCEAN`, `THEME_FOREST`, `THEME_SUNSET`, `THEME_MONO`
- `apply_theme(theme)` - Apply a theme
- `get_theme_color(key)` - Get color from active theme (primary, secondary, success, warning, error, info, highlight, muted)
- `get_current_theme()` - Get current theme
- `list_themes()` - List available themes

**Backward Compatible:** All existing color constants (`RED`, `GREEN`, `CYAN`, etc.) unchanged!

**Example:**
```python
from CB9Lib import *

# Apply Ocean theme
apply_theme(THEME_OCEAN)

# Use theme colors
print(color_text("Success!", fg=get_theme_color('success')))
print(color_text("Warning!", fg=get_theme_color('warning')))
print(color_text("Error!", fg=get_theme_color('error')))

# Switch themes
apply_theme(THEME_FOREST)
apply_theme(THEME_SUNSET)

# OLD colors still work!
print(color_text("Still works!", fg=RED))
```

---

### 8. **Testing Framework** (New module: `testing.py`)
Built-in testing utilities for unit tests.

**New Functions:**
- `assert_equals(actual, expected, msg="")` - Equality assertion
- `assert_true(condition, msg="")` - True assertion
- `assert_false(condition, msg="")` - False assertion
- `test_suite(name)` - Context manager for test grouping
- `mock_input(values)` - Mock user input for testing
- `capture_output()` - Capture print statements
- `get_test_stats()` - Get test statistics
- `reset_test_stats()` - Reset test counters

**Example:**
```python
from CB9Lib.testing import *

with test_suite("Math Tests"):
    assert_equals(2 + 2, 4, "Addition test")
    assert_equals(5 * 5, 25, "Multiplication test")
    assert_true(10 > 5, "Greater than test")
    assert_false(3 > 10, "Less than test")

# Outputs:
# ═══════════════════════════════════════════════
# Test Suite: Math Tests
# ═══════════════════════════════════════════════
# ✓ PASS - Addition test
# ✓ PASS - Multiplication test
# ✓ PASS - Greater than test
# ✓ PASS - Less than test
# ─────────────────────────────────────────────
# Test Results:
#   Total:  4
#   Passed: 4
#   Failed: 0
# ✓ All tests passed!
```

---

## 📦 Package Structure

```
CB9Lib/
├── __init__.py          # Updated exports (v1.3.0)
├── colors.py            # + Themes
├── func.py              # + UI, tables, logging, file utils
├── globals.py           # Unchanged
├── imgvid.py            # Unchanged
├── args.py              # NEW - Command-line parsing
├── validators.py        # NEW - Input validation
└── testing.py           # NEW - Testing utilities
```

---

## 🔄 Import Compatibility

All existing import patterns continue to work:

```python
# Pattern 1: Wildcard (still works)
from CB9Lib import *

# Pattern 2: Specific imports (still works)
from CB9Lib.colors import color_text, RED, GREEN
from CB9Lib.func import header, footerMenu, write_log
from CB9Lib.globals import LOG_DIR

# Pattern 3: New features (opt-in)
from CB9Lib import menu, print_table, Logger
from CB9Lib.validators import is_valid_email
from CB9Lib.args import CB9ArgParser
```

---

## ✅ Backward Compatibility Guarantee

**All 7 existing scripts continue to work without changes:**

1. ✅ `test.py` - All functions work
2. ✅ `imgManager/imgManager.py` - All functions work
3. ✅ `backupMySQL/backupMySQL.py` - All functions work
4. ✅ `aws/awsLS_Snapshot.py` - All functions work
5. ✅ `crontabManager.py` - All functions work
6. ✅ `backup/backup.py` - All functions work
7. ✅ `sftpSync/sftpSync.py` - All functions work

**Why they won't break:**
- No existing function signatures changed
- No existing constants removed or modified
- All existing imports work identically
- New features are additive only
- Existing behavior is preserved

---

## 📊 Statistics

- **Version:** 1.2.0 → 1.3.0
- **New Modules:** 3 (args, validators, testing)
- **New Functions:** 50+
- **Total Exports:** 68 → 105 (+37)
- **Lines of Code Added:** ~1,500
- **Backward Compatibility:** 100%

---

## 🚀 Quick Start

### Installation
```bash
cd /Users/john-ash/Documents/script/CB9Lib
pip install -e .

# With image support
pip install -e ".[images]"
```

### Try the Demo
```bash
python3 example_v13.py
```

### Use in Your Scripts
```python
#!/usr/bin/env python3
from CB9Lib import *

# Use new features
choice = menu("Select option:", ["Option 1", "Option 2", "Option 3"])

databases = select_list("Choose databases:", ["mysql", "postgres"], multi=True)

log = get_logger("MyScript", level=INFO)
log.info("Script started")

headers = ["ID", "Name", "Status"]
rows = [[1, "Server1", "OK"], [2, "Server2", "OK"]]
print_table(headers, rows)
```

---

## 📝 Documentation

- **Full API Reference:** See `README.md`
- **Quick Start Guide:** See `QUICKSTART.md`
- **Live Demo:** Run `python3 example_v13.py`
- **Original Example:** `example.py` still works!

---

## 🙏 Notes

**No scripts will break!** This release was designed with backward compatibility as the top priority. All new features are opt-in additions that enhance the library without affecting existing functionality.

If you encounter any issues, please report them at the GitHub repository.

---

**Enjoy CB9Lib v1.3! 🎉**
