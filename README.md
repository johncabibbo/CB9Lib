# CB9Lib - Cloud Box 9 Python Library

A comprehensive utility library for Cloud Box 9 projects, providing terminal colors, UI components, file operations, and common helper functions.

## Features

- **Terminal Colors**: Full ANSI color support with automatic TTY detection
- **UI Components**: Header/footer menus and banners for CLI applications
- **File Utilities**: JSON config management, file/folder operations, logging
- **Cross-platform**: Works on macOS, Linux, and Windows

## Installation

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

## Quick Start

### Colors

```python
from CB9Lib import color_text, RED, GREEN, YELLOW, BOLD

# Colorized text
print(color_text("Error: Something went wrong!", fg=RED, style=BOLD))
print(color_text("Success!", fg=GREEN))
print(color_text("Warning: Low disk space", fg=YELLOW))

# Test all colors
from CB9Lib import test_colors
test_colors()
```

### UI Components

```python
from CB9Lib import header, footerMenu, clear_screen

# Display a header
header("My Application", "v1.0")

# Display a footer menu and get user input
choice = footerMenu("Select an option from the menu below:")
print(f"You selected: {choice}")
```

### File Operations

```python
from CB9Lib import load_json_config, save_json_config, ensure_folder

# Load JSON configuration
config = load_json_config("settings.json")

# Save JSON configuration
data = {"project": "MyApp", "version": "1.0"}
save_json_config("settings.json", data)

# Ensure a folder exists
ensure_folder("logs")
```

### Logging

```python
from CB9Lib import write_log

# Write to log file and console
write_log("Application started successfully")
write_log("Processing data...")
```

## API Reference

### Colors Module

#### Color Constants
- Standard colors: `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`
- Bright colors: `BRIGHT_BLACK`, `BRIGHT_RED`, `BRIGHT_GREEN`, etc.
- Background colors: `BG_BLACK`, `BG_RED`, etc.
- Styles: `BOLD`, `DIM`, `ITALIC`, `UNDERLINE`, `BLINK`, `INVERSE`, `RESET`

#### Functions
- `color_text(text, fg="", bg="", style="")` - Apply colors and styles to text
- `banner(text, fg=CYAN, style=BOLD)` - Print a centered banner
- `enable_colors(state=True)` - Enable/disable color output
- `test_colors()` - Display color palette
- `color256(code)` - Use 256-color palette
- `rgb(r, g, b)` - Use RGB colors

### Functions Module

#### UI Functions
- `clear_screen()` - Clear the terminal
- `header(title, version)` - Display application header
- `footerMenu(legend)` - Display footer menu and get input
- `pause(msg)` - Pause for user input
- `sleep(seconds)` - Wait with visual indicator

#### File Operations
- `file_exists(path)` - Check if file exists
- `folder_exists(path)` - Check if folder exists
- `ensure_folder(path)` - Create folder if it doesn't exist
- `list_files(path, ext=None)` - List files in directory

#### JSON Operations
- `load_json_config(filename)` - Load JSON configuration file
- `save_json_config(filename, data)` - Save dictionary to JSON file

#### Logging
- `write_log(message, filename=None)` - Write log message to file and console

### Globals Module

#### Constants
- `ROOT_DIR` - Root directory for scripts (`~/Documents/script`)
- `LOG_DIR` - Log directory (`~/Documents/script/logs`)
- `TEMP_DIR` - Temporary directory (`~/Documents/script/temp`)
- `SETTINGS` - Default settings dictionary

#### Functions
- `get_timestamp()` - Get formatted timestamp (YYYY-MM-DD_HH-MM-SS)
- `print_banner(title)` - Print a standard header banner

## Examples

### Complete Application Example

```python
from CB9Lib import (
    header, footerMenu, clear_screen,
    color_text, RED, GREEN, CYAN, BOLD,
    load_json_config, save_json_config,
    write_log
)

def main():
    # Display header
    header("My Application", "v1.0")

    # Log startup
    write_log("Application started")

    # Load configuration
    config = load_json_config("config.json")

    # Display some information
    print(color_text("Welcome to the application!", fg=CYAN, style=BOLD))
    print(color_text(f"Config loaded: {len(config)} items", fg=GREEN))

    # Get user input
    choice = footerMenu("Main Menu")

    if choice == 'q':
        print(color_text("Goodbye!", fg=GREEN))
        write_log("Application exited")
    else:
        print(color_text(f"Processing choice: {choice}", fg=CYAN))

if __name__ == "__main__":
    main()
```

### Custom Color Schemes

```python
from CB9Lib.colors import color_text, rgb, bg_rgb, BOLD

# Use RGB colors
custom_fg = rgb(255, 100, 50)
custom_bg = bg_rgb(20, 20, 40)

print(f"{custom_fg}{custom_bg}{BOLD}Custom colored text!{RESET}")
```

## Requirements

- Python >= 3.10

## License

Copyright (c) 2025 Cloud Box 9 Inc.

## Maintainer

Cloud Box 9 Inc.

## Version History

### v1.1.0 (2025-10-22)
- Initial release as installable package
- Full ANSI color support with TTY detection
- UI components for CLI applications
- File and JSON utilities
- Logging functionality

## Support

For issues, questions, or contributions, please contact Cloud Box 9 Inc.
