# CB9Lib v1.3.0 - Complete API Reference

**Quick reference guide for all functions, classes, and constants in CB9Lib**

---

## 📚 Table of Contents

1. [colors.py](#colorspy) - Terminal colors, styles, and themes
2. [func.py](#funcpy) - Core utilities, UI, tables, logging, files
3. [globals.py](#globalspy) - Global settings and paths
4. [imgvid.py](#imgvidpy) - Image and video utilities
5. [args.py](#argspy) - Command-line argument parsing
6. [validators.py](#validatorspy) - Input validation
7. [testing.py](#testingpy) - Testing framework
8. [Quick Import Guide](#quick-import-guide)

---

## colors.py

**Terminal Colors, Styles, and Themes**

### Color Constants

#### Standard Colors (Foreground)
```python
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
```

#### Bright Colors (Foreground)
```python
BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW
BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE
```

#### Background Colors
```python
BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW
BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE
```

#### Bright Background Colors
```python
BG_BRIGHT_BLACK, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW
BG_BRIGHT_BLUE, BG_BRIGHT_MAGENTA, BG_BRIGHT_CYAN, BG_BRIGHT_WHITE
```

#### Style Modifiers
```python
BOLD, DIM, ITALIC, UNDERLINE, BLINK, INVERSE, HIDDEN, STRIKE, RESET
```

---

### Functions

#### `color_text(text, fg="", bg="", style="") -> str`
Apply color and style to text.

**Parameters:**
- `text` (str): Text to colorize
- `fg` (str): Foreground color (e.g., RED, GREEN, CYAN)
- `bg` (str): Background color (e.g., BG_BLACK, BG_BLUE)
- `style` (str): Style modifier (e.g., BOLD, ITALIC, UNDERLINE)

**Returns:** Formatted string with ANSI codes

**Example:**
```python
from CB9Lib import color_text, RED, GREEN, BOLD

print(color_text("Error!", fg=RED, style=BOLD))
print(color_text("Success", fg=GREEN))
print(color_text("Warning", fg=YELLOW, bg=BG_BLACK))
```

---

#### `banner(text, fg=CYAN, style=BOLD)`
Print a centered banner with borders.

**Parameters:**
- `text` (str): Banner text
- `fg` (str): Foreground color (default: CYAN)
- `style` (str): Style modifier (default: BOLD)

**Example:**
```python
from CB9Lib import banner

banner("Welcome to My App")
```

---

#### `enable_colors(state=True)`
Manually enable or disable color output.

**Parameters:**
- `state` (bool): True to enable, False to disable

**Example:**
```python
from CB9Lib import enable_colors, color_text, RED

enable_colors(False)  # Disable colors
print(color_text("No color", fg=RED))

enable_colors(True)   # Re-enable
print(color_text("With color!", fg=RED))
```

---

#### `color256(code) -> str`
Use 256-color palette (0-255).

**Parameters:**
- `code` (int): Color code (0-255)

**Returns:** ANSI escape code

**Example:**
```python
from CB9Lib import color256

print(f"{color256(196)}Red text{RESET}")
```

---

#### `bg256(code) -> str`
Use 256-color palette for background (0-255).

**Parameters:**
- `code` (int): Color code (0-255)

**Returns:** ANSI escape code

---

#### `rgb(r, g, b) -> str`
Use RGB color (true color).

**Parameters:**
- `r` (int): Red value (0-255)
- `g` (int): Green value (0-255)
- `b` (int): Blue value (0-255)

**Returns:** ANSI escape code

**Example:**
```python
from CB9Lib import rgb, RESET

print(f"{rgb(255, 100, 50)}Custom color{RESET}")
```

---

#### `bg_rgb(r, g, b) -> str`
Use RGB color for background.

**Parameters:**
- `r` (int): Red value (0-255)
- `g` (int): Green value (0-255)
- `b` (int): Blue value (0-255)

**Returns:** ANSI escape code

---

#### `test_colors()`
Display all available colors.

**Example:**
```python
from CB9Lib import test_colors

test_colors()
```

---

### Color Themes (v1.3)

#### Theme Constants
```python
THEME_DEFAULT   # Cyan/Magenta theme
THEME_OCEAN     # Blue/Cyan ocean theme
THEME_FOREST    # Green/Cyan forest theme
THEME_SUNSET    # Magenta/Yellow sunset theme
THEME_MONO      # Monochrome theme
```

Each theme has these keys:
- `primary` - Primary accent color
- `secondary` - Secondary accent color
- `success` - Success/OK color
- `warning` - Warning color
- `error` - Error color
- `info` - Information color
- `highlight` - Highlight color
- `muted` - Muted/dim color

---

#### `apply_theme(theme)`
Apply a color theme.

**Parameters:**
- `theme` (dict): Theme dictionary (e.g., THEME_OCEAN)

**Example:**
```python
from CB9Lib import apply_theme, THEME_OCEAN, get_theme_color, color_text

apply_theme(THEME_OCEAN)
print(color_text("Success!", fg=get_theme_color('success')))
print(color_text("Warning!", fg=get_theme_color('warning')))
```

---

#### `get_theme_color(key) -> str`
Get a color from the active theme.

**Parameters:**
- `key` (str): Theme key (primary, secondary, success, warning, error, info, highlight, muted)

**Returns:** ANSI color code

**Example:**
```python
from CB9Lib import get_theme_color, color_text

primary = get_theme_color('primary')
print(color_text("Primary color text", fg=primary))
```

---

#### `get_current_theme() -> dict`
Get the currently active theme dictionary.

**Returns:** Dictionary of current theme colors

---

#### `list_themes() -> list`
List all available theme names.

**Returns:** List of theme names ['DEFAULT', 'OCEAN', 'FOREST', 'SUNSET', 'MONO']

---

## func.py

**Core Utilities, UI Components, Tables, Logging, and File Operations**

### Core Utilities

#### `clear_screen()`
Clear the terminal screen (cross-platform).

**Example:**
```python
from CB9Lib import clear_screen

clear_screen()
```

---

#### `pause(msg="Press Enter to continue...")`
Pause execution and wait for user to press Enter.

**Parameters:**
- `msg` (str): Message to display

**Example:**
```python
from CB9Lib import pause

pause()
pause("Press Enter when ready...")
```

---

#### `sleep(seconds=1.0)`
Wait for N seconds with visual indicator.

**Parameters:**
- `seconds` (float): Number of seconds to wait

**Example:**
```python
from CB9Lib import sleep

sleep(2.5)  # Wait 2.5 seconds
```

---

### JSON Helpers

#### `load_json_config(jsonFileName) -> dict`
Load and parse JSON config file.

**Parameters:**
- `jsonFileName` (str): Path to JSON file

**Returns:** Dictionary of config data, empty dict {} on error

**Example:**
```python
from CB9Lib import load_json_config

config = load_json_config("config.json")
if config:
    db_host = config.get('database', {}).get('host')
```

---

#### `save_json_config(jsonFileName, data)`
Save dictionary to JSON file with indentation.

**Parameters:**
- `jsonFileName` (str): Path to JSON file
- `data` (dict): Dictionary to save

**Example:**
```python
from CB9Lib import save_json_config

config = {
    "database": {"host": "localhost", "port": 3306},
    "backup_dir": "/backups"
}
save_json_config("config.json", config)
```

---

### UI Elements

#### `header(title="Untitled Script", version="v1.2", subtitle="", width=0)`
Display a full header banner with title and version.

**Parameters:**
- `title` (str): Script/application title
- `version` (str): Version string
- `subtitle` (str): Optional subtitle text
- `width` (int): Terminal width (0 = auto-detect)

**Example:**
```python
from CB9Lib import header

header("Backup Manager", "v2.1", "MySQL Database Backup")
```

---

#### `footerMenu(legend="", width=0) -> str`
Display footer menu with legend and prompt for user input.

**Parameters:**
- `legend` (str): Menu legend/instructions
- `width` (int): Terminal width (0 = auto-detect)

**Returns:** User's input choice (string)

**Example:**
```python
from CB9Lib import footerMenu

choice = footerMenu("(Q)uit | (B)ackup | (R)estore")
if choice == 'q':
    print("Quitting...")
elif choice == 'b':
    print("Starting backup...")
```

---

### Interactive UI (v1.3)

#### `menu(title, options, allow_back=True, allow_quit=True) -> str`
Display an interactive menu with numbered options.

**Parameters:**
- `title` (str): Menu title
- `options` (list): List of menu options (strings)
- `allow_back` (bool): Include 'Back' option (default: True)
- `allow_quit` (bool): Include 'Quit' option (default: True)

**Returns:** User's choice ('1', '2', 'back', 'quit')

**Example:**
```python
from CB9Lib import menu

choice = menu("Main Menu", [
    "Full Backup",
    "Incremental Backup",
    "Restore",
    "Settings"
])

if choice == '1':
    print("Starting full backup...")
elif choice == '2':
    print("Starting incremental backup...")
elif choice == 'quit':
    print("Exiting...")
```

---

#### `select_list(title, items, multi=False, selected=None) -> list`
Interactive item selection with number input.

**Parameters:**
- `title` (str): Selection prompt
- `items` (list): List of items to choose from
- `multi` (bool): Allow multiple selections (default: False)
- `selected` (list): Pre-selected items (default: None)

**Returns:** List of selected items

**Example:**
```python
from CB9Lib import select_list

# Single selection
databases = ["mysql_prod", "mysql_dev", "postgres_app"]
selected = select_list("Select database:", databases, multi=False)
print(f"Selected: {selected[0]}")

# Multi-selection
selected = select_list("Select databases to backup:", databases, multi=True)
print(f"Will backup: {', '.join(selected)}")
```

---

#### `progress_bar(current, total, width=50, label="", show_percent=True)`
Display a progress bar in the terminal.

**Parameters:**
- `current` (int): Current progress value
- `total` (int): Total/maximum value
- `width` (int): Bar width in characters (default: 50)
- `label` (str): Optional label before the bar
- `show_percent` (bool): Show percentage (default: True)

**Example:**
```python
from CB9Lib import progress_bar
import time

for i in range(1, 101):
    progress_bar(i, 100, label="Processing files", width=50)
    time.sleep(0.05)  # Simulate work
```

---

#### `confirm(prompt, default=True) -> bool`
Ask for yes/no confirmation.

**Parameters:**
- `prompt` (str): Question to ask
- `default` (bool): Default answer if Enter pressed

**Returns:** True for yes, False for no

**Example:**
```python
from CB9Lib import confirm

if confirm("Delete all old backups?", default=False):
    print("Deleting backups...")
else:
    print("Keeping backups.")
```

---

### Table Formatting (v1.3)

#### `print_table(headers, rows, align=None, border=True)`
Print a formatted table to the console.

**Parameters:**
- `headers` (list): List of column headers
- `rows` (list): List of lists (each inner list is a row)
- `align` (list): List of alignment per column ('left', 'right', 'center')
- `border` (bool): Show border lines (default: True)

**Example:**
```python
from CB9Lib import print_table

headers = ["Snapshot ID", "Size", "Status", "Date"]
rows = [
    ["snap-001", "8.5 GB", "Complete", "2024-10-20"],
    ["snap-002", "8.7 GB", "Complete", "2024-10-21"],
    ["snap-003", "8.3 GB", "Partial", "2024-10-22"]
]
print_table(headers, rows, align=['left', 'right', 'center', 'left'])
```

**Output:**
```
┌─────────────────────────────────────────────────┐
│ Snapshot ID │     Size │  Status  │ Date       │
├─────────────────────────────────────────────────┤
│ snap-001    │  8.5 GB  │ Complete │ 2024-10-20 │
│ snap-002    │  8.7 GB  │ Complete │ 2024-10-21 │
│ snap-003    │  8.3 GB  │ Partial  │ 2024-10-22 │
└─────────────────────────────────────────────────┘
```

---

#### `table_format(headers, rows, align=None) -> str`
Return a formatted table as a string (for logging).

**Parameters:**
- `headers` (list): List of column headers
- `rows` (list): List of lists (each inner list is a row)
- `align` (list): List of alignment per column

**Returns:** Formatted table string

**Example:**
```python
from CB9Lib import table_format, write_log

headers = ["ID", "Status"]
rows = [[1, "OK"], [2, "Fail"]]
table_str = table_format(headers, rows)
write_log(table_str, "report.log")
```

---

#### `print_dict_table(dict_list, keys=None)`
Print a table from a list of dictionaries.

**Parameters:**
- `dict_list` (list): List of dictionaries
- `keys` (list): Specific keys to display (None = all keys)

**Example:**
```python
from CB9Lib import print_dict_table

backups = [
    {"name": "mysql_prod", "size": "2.4 GB", "status": "OK"},
    {"name": "postgres_app", "size": "1.8 GB", "status": "OK"},
    {"name": "redis_cache", "size": "512 MB", "status": "OK"}
]
print_dict_table(backups)

# Or specific columns only
print_dict_table(backups, keys=["name", "status"])
```

---

### File Utilities

#### `file_exists(path) -> bool`
Check if a file exists.

**Parameters:**
- `path` (str): Path to file

**Returns:** True if file exists, False otherwise

**Example:**
```python
from CB9Lib import file_exists

if file_exists("backup.tar"):
    print("Backup file found")
```

---

#### `folder_exists(path) -> bool`
Check if a directory exists.

**Parameters:**
- `path` (str): Path to directory

**Returns:** True if directory exists, False otherwise

**Example:**
```python
from CB9Lib import folder_exists

if not folder_exists("/backups"):
    print("Backup directory not found!")
```

---

#### `ensure_folder(path)`
Create directory if it doesn't exist.

**Parameters:**
- `path` (str): Path to directory

**Example:**
```python
from CB9Lib import ensure_folder

ensure_folder("/backups/mysql")
ensure_folder("/logs")
```

---

#### `list_files(path, ext=None) -> list`
List files in a directory, optionally filter by extension.

**Parameters:**
- `path` (str): Directory path
- `ext` (str): Optional file extension filter (e.g., ".py", ".json")

**Returns:** Sorted list of filenames

**Example:**
```python
from CB9Lib import list_files

# All files
all_files = list_files("/backups")

# Only .tar files
tar_files = list_files("/backups", ext=".tar")
print(f"Found {len(tar_files)} tar files")
```

---

#### `remove_files(path, filelist=None, dry_run=False, log_deletions=True) -> bool`
Delete files matching patterns from path recursively.

**Parameters:**
- `path` (str): Root directory to search
- `filelist` (list): List of patterns (e.g., ['.DS_Store', '*.tmp', '*.log'])
- `dry_run` (bool): Test mode - show what would be deleted (default: False)
- `log_deletions` (bool): Log deletions to LOG_DIR (default: True)

**Returns:** True if successful, False if errors occurred

**Example:**
```python
from CB9Lib import remove_files

# Dry run first to see what will be deleted
remove_files("/Volumes/Data", ['.DS_Store', '*.tmp'], dry_run=True)

# Actually delete
remove_files("/Volumes/Data", ['.DS_Store', '*.tmp', '._*'])
```

---

### Advanced File Utilities (v1.3)

#### `copy_file(src, dst, overwrite=False) -> bool`
Copy a file from source to destination.

**Parameters:**
- `src` (str): Source file path
- `dst` (str): Destination file path
- `overwrite` (bool): Allow overwriting existing file (default: False)

**Returns:** True if successful, False otherwise

**Example:**
```python
from CB9Lib import copy_file

copy_file("/backups/old/backup.tar", "/backups/new/backup.tar")
copy_file("config.json", "config.backup.json", overwrite=True)
```

---

#### `move_file(src, dst) -> bool`
Move a file from source to destination.

**Parameters:**
- `src` (str): Source file path
- `dst` (str): Destination file path

**Returns:** True if successful, False otherwise

**Example:**
```python
from CB9Lib import move_file

move_file("/tmp/backup.tar", "/backups/backup.tar")
```

---

#### `search_files(path, pattern, recursive=True) -> list`
Search for files matching a pattern.

**Parameters:**
- `path` (str): Directory to search
- `pattern` (str): Glob pattern (e.g., "*.py", "backup_*")
- `recursive` (bool): Search subdirectories (default: True)

**Returns:** List of matching file paths

**Example:**
```python
from CB9Lib import search_files

# Find all Python files recursively
python_files = search_files("/project", "*.py", recursive=True)

# Find backup files in current directory only
backups = search_files("/backups", "backup_*.tar", recursive=False)

print(f"Found {len(python_files)} Python files")
```

---

#### `get_file_info(path) -> dict`
Get detailed information about a file.

**Parameters:**
- `path` (str): File path

**Returns:** Dictionary with file info:
- `path` - Absolute path
- `name` - Filename
- `size_bytes` - Size in bytes
- `size_mb` - Size in MB
- `modified` - Last modified date/time
- `created` - Creation date/time
- `is_file` - True if file
- `is_dir` - True if directory
- `extension` - File extension

**Example:**
```python
from CB9Lib import get_file_info

info = get_file_info("backup.tar")
print(f"File: {info['name']}")
print(f"Size: {info['size_mb']} MB")
print(f"Modified: {info['modified']}")
print(f"Extension: {info['extension']}")
```

---

### Logging (Original)

#### `write_log(message, filename=None)`
Write a log message to file and print to console.

**Parameters:**
- `message` (str): Log message
- `filename` (str): Optional log file path (auto-generated if None)

**Example:**
```python
from CB9Lib import write_log

write_log("Backup started", "backup.log")
write_log("Processing 100 files", "backup.log")
write_log("Backup completed", "backup.log")
```

---

#### `log_header(job_name, version="v1.2", filename=None) -> str`
Write log header at start of job.

**Parameters:**
- `job_name` (str): Name of the job/script
- `version` (str): Version string
- `filename` (str): Optional log file path (auto-generated if None)

**Returns:** Log filename

**Example:**
```python
from CB9Lib import log_header, write_log, log_footer

log_file = log_header("MySQL Backup", "v2.1")
write_log("Starting backup...", log_file)
write_log("Backup complete", log_file)
log_footer("MySQL Backup", "v2.1", log_file)
```

---

#### `log_footer(job_name, version="v1.2", filename=None)`
Write log footer at end of job.

**Parameters:**
- `job_name` (str): Name of the job/script
- `version` (str): Version string
- `filename` (str): Log file path

**Example:**
```python
from CB9Lib import log_footer

log_footer("MySQL Backup", "v2.1", log_file)
```

---

#### `logRotate(script_name, version="v1.2", old_filename=None) -> str`
Rotate log file and create a new one with header.

**Parameters:**
- `script_name` (str): Name of the script/job
- `version` (str): Version string
- `old_filename` (str): Optional previous log file to close

**Returns:** Path to new log file

**Example:**
```python
from CB9Lib import logRotate, write_log

log_file = logRotate("BackupScript", "v1.0")
write_log("New log started", log_file)

# Later, rotate again
log_file = logRotate("BackupScript", "v1.0", old_filename=log_file)
```

---

### Advanced Logging (v1.3)

#### Log Level Constants
```python
DEBUG = 10      # Detailed debugging information
INFO = 20       # General informational messages
WARNING = 30    # Warning messages
ERROR = 40      # Error messages
CRITICAL = 50   # Critical errors
```

---

#### `Logger` Class
Advanced logger with level filtering.

**Constructor:**
```python
Logger(name, level=INFO, filename=None, console=True, colored=True)
```

**Parameters:**
- `name` (str): Logger name (usually script/module name)
- `level` (int): Minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `filename` (str): Optional log file path
- `console` (bool): Print to console (default: True)
- `colored` (bool): Use colors in console output (default: True)

**Methods:**
- `logger.debug(message)` - Log debug message
- `logger.info(message)` - Log info message
- `logger.warning(message)` - Log warning message
- `logger.error(message)` - Log error message
- `logger.critical(message)` - Log critical message
- `logger.set_level(level)` - Change log level dynamically

**Example:**
```python
from CB9Lib import Logger, INFO, DEBUG, WARNING

log = Logger("MyApp", level=INFO, filename="app.log")

log.debug("This won't show (below INFO level)")
log.info("Application started")
log.warning("Low disk space: 10%")
log.error("Failed to connect to database")
log.critical("System shutdown")

# Change level
log.set_level(DEBUG)
log.debug("Now debug messages appear")
```

---

#### `get_logger(name, level=INFO, filename=None) -> Logger`
Create and return a Logger instance (convenience function).

**Parameters:**
- `name` (str): Logger name
- `level` (int): Minimum log level
- `filename` (str): Optional log file

**Returns:** Logger instance

**Example:**
```python
from CB9Lib import get_logger, INFO, WARNING

log = get_logger("BackupScript", level=INFO, filename="backup.log")
log.info("Backup started")
log.warning("Low disk space")
```

---

### Testing

#### `test_ui()`
Demonstrate header, footer, and color usage.

**Example:**
```python
from CB9Lib import test_ui

test_ui()
```

---

## globals.py

**Global Settings, Paths, and Constants**

### Global Path Constants

```python
ROOT_DIR   # ~/Documents/script
LOG_DIR    # ~/Documents/logs
TEMP_DIR   # ~/Documents/script/temp
```

**Example:**
```python
from CB9Lib import LOG_DIR, TEMP_DIR

log_path = f"{LOG_DIR}/backup.log"
temp_path = f"{TEMP_DIR}/processing"
```

---

### Functions

#### `get_timestamp() -> str`
Returns current timestamp in "YYYY-MM-DD_HH-MM-SS" format.

**Returns:** Timestamp string

**Example:**
```python
from CB9Lib import get_timestamp

timestamp = get_timestamp()  # "2024-10-25_14-30-45"
filename = f"backup_{timestamp}.tar"
```

---

#### `print_banner(title)`
Print styled banner.

**Parameters:**
- `title` (str): Banner title

**Example:**
```python
from CB9Lib import print_banner

print_banner("Backup Manager v2.0")
```

---

### Settings Dictionary

```python
SETTINGS = {
    "project": "SharedLibrary",
    "version": "1.2",
    "log_folder": LOG_DIR,
    "temp_folder": TEMP_DIR
}
```

**Example:**
```python
from CB9Lib import SETTINGS

project_name = SETTINGS['project']
log_folder = SETTINGS['log_folder']
```

---

## imgvid.py

**Image and Video Utilities**

### Functions

#### `create_thumb_resize(src_path, max_width=150, max_height=150, suffix="_tmb") -> str|bool`
Create a thumbnail from an image.

**Parameters:**
- `src_path` (str): Path to source image
- `max_width` (int): Maximum thumbnail width (default: 150)
- `max_height` (int): Maximum thumbnail height (default: 150)
- `suffix` (str): Filename suffix (default: "_tmb")

**Returns:** Path to thumbnail or False on failure

**Requirements:** Pillow library (`pip install Pillow`)

**Example:**
```python
from CB9Lib import create_thumb_resize

# Create thumbnail
thumb_path = create_thumb_resize("photo.jpg", max_width=200, max_height=200)
if thumb_path:
    print(f"Thumbnail created: {thumb_path}")
```

---

#### `list_thumbnails(image_directory) -> list`
Find all thumbnail files in a directory.

**Parameters:**
- `image_directory` (str): Directory to search

**Returns:** List of thumbnail filenames (ending in "_tmb.jpg")

**Example:**
```python
from CB9Lib import list_thumbnails

thumbnails = list_thumbnails("/photos")
print(f"Found {len(thumbnails)} thumbnails")
```

---

## args.py

**Command-Line Argument Parsing**

### Functions

#### `parse_simple_args(expected_args=None) -> dict`
Simple argument parser for scripts.

**Parameters:**
- `expected_args` (list): List of expected argument names

**Returns:** Dictionary of argument names to values

**Example:**
```python
from CB9Lib.args import parse_simple_args

# Script called as: python script.py db1 db2 --dry-run --verbose
args = parse_simple_args(['database', 'target'])

# Returns: {'database': 'db1', 'target': 'db2', 'dry_run': True, 'verbose': True}
print(f"Database: {args['database']}")
print(f"Target: {args['target']}")
print(f"Dry run: {args.get('dry_run', False)}")
```

---

#### `CB9ArgParser` Class
Enhanced argument parser with CB9Lib styling.

**Constructor:**
```python
CB9ArgParser(name, version, description="")
```

**Parameters:**
- `name` (str): Script/program name
- `version` (str): Version string
- `description` (str): Optional description text

**Methods:**
- `add_argument(*args, **kwargs)` - Add argument (same as argparse)
- `parse()` - Parse and return argparse.Namespace
- `parse_dict()` - Parse and return dictionary

**Example:**
```python
from CB9Lib.args import CB9ArgParser

parser = CB9ArgParser("Backup Manager", "v2.0", "MySQL backup automation")
parser.add_argument('database', help='Database name')
parser.add_argument('--output', '-o', default='./backups', help='Output directory')
parser.add_argument('--compress', action='store_true', help='Compress backup')
parser.add_argument('--rotate', type=int, default=7, help='Days to keep')

args = parser.parse()

print(f"Database: {args.database}")
print(f"Output: {args.output}")
print(f"Compress: {args.compress}")
print(f"Rotate: {args.rotate} days")
```

---

#### `get_script_name() -> str`
Get the name of the running script.

**Returns:** Script name

**Example:**
```python
from CB9Lib.args import get_script_name

script = get_script_name()  # "/path/to/script.py"
```

---

#### `get_all_args() -> list`
Get all command-line arguments (excluding script name).

**Returns:** List of arguments

**Example:**
```python
from CB9Lib.args import get_all_args

args = get_all_args()  # ['db1', '--dry-run', '--verbose']
```

---

## validators.py

**Input Validation Utilities**

### Validation Functions

#### `is_valid_email(email) -> bool`
Validate email address format.

**Parameters:**
- `email` (str): Email address to validate

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_email

if is_valid_email("user@example.com"):
    print("Valid email")
else:
    print("Invalid email")
```

---

#### `is_valid_number(value, min_val=None, max_val=None) -> bool`
Validate number and optional range.

**Parameters:**
- `value` (str): Value to validate
- `min_val` (float): Optional minimum value
- `max_val` (float): Optional maximum value

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_number

if is_valid_number("42", min_val=0, max_val=100):
    print("Valid number in range")
```

---

#### `is_valid_integer(value, min_val=None, max_val=None) -> bool`
Validate integer and optional range.

**Parameters:**
- `value` (str): Value to validate
- `min_val` (int): Optional minimum value
- `max_val` (int): Optional maximum value

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_integer

if is_valid_integer("42", min_val=1, max_val=100):
    print("Valid integer")
```

---

#### `is_valid_path(path, must_exist=False, must_be_file=False, must_be_dir=False) -> bool`
Validate file/directory path.

**Parameters:**
- `path` (str): Path to validate
- `must_exist` (bool): Path must exist (default: False)
- `must_be_file` (bool): Path must be a file (default: False)
- `must_be_dir` (bool): Path must be a directory (default: False)

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_path

if is_valid_path("/backups", must_exist=True, must_be_dir=True):
    print("Backup directory exists")

if is_valid_path("config.json", must_exist=True, must_be_file=True):
    print("Config file exists")
```

---

#### `is_valid_ip(ip, version=4) -> bool`
Validate IP address (IPv4 or IPv6).

**Parameters:**
- `ip` (str): IP address to validate
- `version` (int): IP version (4 or 6, default: 4)

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_ip

if is_valid_ip("192.168.1.1"):
    print("Valid IPv4")

if is_valid_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334", version=6):
    print("Valid IPv6")
```

---

#### `is_valid_hostname(hostname) -> bool`
Validate hostname format.

**Parameters:**
- `hostname` (str): Hostname to validate

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_hostname

if is_valid_hostname("server.example.com"):
    print("Valid hostname")
```

---

#### `is_valid_port(port) -> bool`
Validate port number (1-65535).

**Parameters:**
- `port` (str): Port number to validate

**Returns:** True if valid, False otherwise

**Example:**
```python
from CB9Lib.validators import is_valid_port

if is_valid_port("3306"):
    print("Valid port")
```

---

### Interactive Validation

#### `validate_input(prompt, validator, error_msg="Invalid input. Please try again.", max_attempts=3) -> str|None`
Prompt for input with validation.

**Parameters:**
- `prompt` (str): Input prompt text
- `validator` (callable): Function that returns True if input is valid
- `error_msg` (str): Error message for invalid input
- `max_attempts` (int): Maximum attempts (0 = unlimited)

**Returns:** Valid input string, or None if max attempts exceeded

**Example:**
```python
from CB9Lib.validators import validate_input, is_valid_email, is_valid_number

# Email validation
email = validate_input(
    "Enter your email:",
    is_valid_email,
    "Invalid email format. Please try again."
)

# Number validation with lambda
port = validate_input(
    "Enter MySQL port:",
    lambda x: is_valid_number(x, min_val=1024, max_val=65535),
    "Port must be between 1024 and 65535"
)
```

---

#### `validate_choice(prompt, valid_choices, case_sensitive=False) -> str|None`
Prompt for input from a list of valid choices.

**Parameters:**
- `prompt` (str): Input prompt text
- `valid_choices` (list): List of valid choices
- `case_sensitive` (bool): Case-sensitive matching (default: False)

**Returns:** Selected choice (properly cased), or None if validation fails

**Example:**
```python
from CB9Lib.validators import validate_choice

env = validate_choice(
    "Select environment",
    ["dev", "staging", "prod"]
)
print(f"Environment: {env}")

# Case-sensitive
db_type = validate_choice(
    "Database type",
    ["MySQL", "PostgreSQL", "MongoDB"],
    case_sensitive=True
)
```

---

## testing.py

**Testing Framework Utilities**

### Assertion Functions

#### `assert_equals(actual, expected, msg="") -> bool`
Simple equality assertion.

**Parameters:**
- `actual` (any): Actual value
- `expected` (any): Expected value
- `msg` (str): Optional message

**Returns:** True if passes, False if fails

**Example:**
```python
from CB9Lib.testing import assert_equals

assert_equals(2 + 2, 4, "Addition test")
assert_equals(len([1,2,3]), 3, "List length test")
assert_equals("hello".upper(), "HELLO", "String uppercase test")
```

---

#### `assert_true(condition, msg="") -> bool`
Assert that condition is True.

**Parameters:**
- `condition` (bool): Boolean condition
- `msg` (str): Optional message

**Returns:** True if passes, False if fails

**Example:**
```python
from CB9Lib.testing import assert_true

assert_true(10 > 5, "10 is greater than 5")
assert_true("hello" in "hello world", "Substring test")
```

---

#### `assert_false(condition, msg="") -> bool`
Assert that condition is False.

**Parameters:**
- `condition` (bool): Boolean condition
- `msg` (str): Optional message

**Returns:** True if passes, False if fails

**Example:**
```python
from CB9Lib.testing import assert_false

assert_false(5 > 10, "5 is not greater than 10")
assert_false("xyz" in "hello", "xyz not in hello")
```

---

### Test Organization

#### `test_suite(name)` Context Manager
Group tests together with automatic reporting.

**Parameters:**
- `name` (str): Test suite name

**Example:**
```python
from CB9Lib.testing import test_suite, assert_equals, assert_true

with test_suite("Math Operations"):
    assert_equals(2 + 2, 4, "Addition")
    assert_equals(5 * 5, 25, "Multiplication")
    assert_true(10 > 5, "Comparison")

# Output:
# ════════════════════════════════════════════════════════════
# Test Suite: Math Operations
# ════════════════════════════════════════════════════════════
# ✓ PASS - Addition
# ✓ PASS - Multiplication
# ✓ PASS - Comparison
# ────────────────────────────────────────────────────────────
# Test Results:
#   Total:  3
#   Passed: 3
#   Failed: 0
# ✓ All tests passed!
```

---

### Test Utilities

#### `mock_input(values)` Context Manager
Mock user input for testing.

**Parameters:**
- `values` (list): List of input values to return in sequence

**Example:**
```python
from CB9Lib.testing import mock_input, assert_equals

with mock_input(["John", "25"]):
    name = input("Name: ")
    age = input("Age: ")

assert_equals(name, "John")
assert_equals(age, "25")
```

---

#### `capture_output()` Context Manager
Capture print statements for testing.

**Returns:** StringIO object with captured output

**Example:**
```python
from CB9Lib.testing import capture_output, assert_equals

with capture_output() as output:
    print("Hello, World!")
    print("Testing")

captured = output.getvalue()
assert_equals(captured, "Hello, World!\nTesting\n")
```

---

#### `get_test_stats() -> dict`
Get current test statistics.

**Returns:** Dictionary with 'passed', 'failed', 'total' counts

**Example:**
```python
from CB9Lib.testing import get_test_stats

stats = get_test_stats()
print(f"Passed: {stats['passed']}, Failed: {stats['failed']}")
```

---

#### `reset_test_stats()`
Reset test statistics to zero.

**Example:**
```python
from CB9Lib.testing import reset_test_stats

reset_test_stats()
```

---

## Quick Import Guide

### Common Patterns

#### Import Everything
```python
from CB9Lib import *

# Access all functions directly
header("My App", "v1.0")
choice = menu("Menu", ["Option 1", "Option 2"])
print_table(["Col1", "Col2"], [["A", "B"]])
```

#### Import Specific Functions
```python
from CB9Lib import header, menu, print_table, color_text, RED, GREEN

header("My App", "v1.0")
print(color_text("Success", fg=GREEN))
```

#### Import Modules
```python
from CB9Lib import colors, func, validators

print(colors.color_text("Hello", fg=colors.RED))
func.header("My App", "v1.0")
if validators.is_valid_email(email):
    print("Valid")
```

#### Import Specific Modules
```python
from CB9Lib.colors import color_text, RED, GREEN, CYAN
from CB9Lib.func import header, menu, print_table
from CB9Lib.validators import is_valid_email, validate_input
from CB9Lib.testing import test_suite, assert_equals
```

---

## Complete Example Script

```python
#!/usr/bin/env python3
"""
Complete example using multiple CB9Lib features
"""
from CB9Lib import *

def main():
    # 1. Display header
    header("Database Backup Manager", "v2.0", "Automated MySQL Backup")

    # 2. Select databases with interactive menu
    databases = ["mysql_prod", "mysql_dev", "postgres_app", "redis_cache"]
    selected = select_list("Select databases to backup:", databases, multi=True)

    if not selected:
        print(color_text("No databases selected!", fg=RED))
        return

    # 3. Confirm action
    if not confirm(f"Backup {len(selected)} database(s)?", default=True):
        print(color_text("Backup cancelled", fg=YELLOW))
        return

    # 4. Setup logging
    log = get_logger("BackupManager", level=INFO, filename="backup.log")
    log.info(f"Starting backup of {len(selected)} databases")

    # 5. Process with progress bar
    backup_results = []
    for i, db in enumerate(selected, 1):
        progress_bar(i, len(selected), label="Backing up databases")

        # Simulate backup
        import time
        time.sleep(0.5)

        log.info(f"Backed up {db}")
        backup_results.append({
            "database": db,
            "size": f"{i * 2.5:.1f} GB",
            "status": "✓ Complete"
        })

    # 6. Display results in table
    print("\n")
    print(color_text("Backup Results:", fg=BRIGHT_CYAN, style=BOLD))
    print_dict_table(backup_results)

    # 7. Log completion
    log.info("All backups completed successfully")
    print("\n" + color_text("✓ Backup complete!", fg=BRIGHT_GREEN, style=BOLD))

    pause()

if __name__ == "__main__":
    main()
```

---

## Version History

- **v1.3.0** (2025-10-25) - Added interactive UI, tables, advanced logging, validation, testing, themes
- **v1.2.0** (2025-10-23) - Added log rotation, enhanced documentation
- **v1.1.0** (2025-10-22) - Added basic logging functions

---

**For more information, see:**
- `README.md` - Overview and installation
- `QUICKSTART.md` - Quick start guide
- `CHANGELOG_v1.3.md` - Complete v1.3 changelog
- `example_v13.py` - Interactive demo

---

**CB9Lib v1.3.0** - Cloud Box 9 Inc. - MIT License
