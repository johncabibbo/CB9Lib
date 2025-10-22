# CB9Lib Quick Start Guide

## Installation

### Local Development Installation

```bash
# Navigate to the CB9Lib directory
cd CB9Lib

# Install in editable/development mode
pip install -e .
```

### Install from Git Repository

```bash
pip install git+https://github.com/yourusername/CB9Lib.git
```

## Basic Usage

### 1. Import the Library

```python
# Import specific functions and colors
from CB9Lib import color_text, RED, GREEN, BOLD

# Or import everything
from CB9Lib import *
```

### 2. Simple Color Example

```python
from CB9Lib import color_text, RED, GREEN, YELLOW, BOLD

print(color_text("Error message", fg=RED, style=BOLD))
print(color_text("Success message", fg=GREEN))
print(color_text("Warning message", fg=YELLOW))
```

### 3. Create a CLI Application

```python
from CB9Lib import header, footerMenu, color_text, GREEN, CYAN

# Display header
header("My Application", "v1.0")

# Show some content
print(color_text("Welcome to my application!", fg=CYAN))
print(color_text("Processing complete.", fg=GREEN))

# Get user input with footer menu
choice = footerMenu("Main Menu")
print(f"You selected: {choice}")
```

### 4. Work with JSON Files

```python
from CB9Lib import load_json_config, save_json_config

# Save configuration
config = {
    "database": "mydb.db",
    "timeout": 30,
    "debug": True
}
save_json_config("config.json", config)

# Load configuration
loaded = load_json_config("config.json")
print(f"Database: {loaded['database']}")
```

### 5. File Operations and Logging

```python
from CB9Lib import ensure_folder, write_log, file_exists

# Create directories if needed
ensure_folder("logs")
ensure_folder("data")

# Write to log
write_log("Application started")
write_log("Processing 100 records")

# Check if file exists
if file_exists("config.json"):
    print("Config file found!")
```

## Common Patterns

### Terminal Output with Colors

```python
from CB9Lib import color_text, banner
from CB9Lib import RED, GREEN, YELLOW, CYAN, BOLD

# Status messages
print(color_text("✓ Task completed", fg=GREEN))
print(color_text("⚠ Warning: Low memory", fg=YELLOW))
print(color_text("✗ Error: File not found", fg=RED, style=BOLD))

# Section headers
banner("Processing Data", fg=CYAN)
```

### Complete Application Template

```python
#!/usr/bin/env python3

from CB9Lib import (
    header, footerMenu, clear_screen,
    color_text, banner,
    RED, GREEN, YELLOW, CYAN, BOLD,
    load_json_config, save_json_config,
    write_log, ensure_folder
)

def main():
    # Setup
    ensure_folder("logs")
    write_log("Application started")

    # Display UI
    header("My Application", "v1.0")

    # Load config
    config = load_json_config("config.json")

    # Show content
    banner("Main Section")
    print(color_text("Application is running...", fg=CYAN))

    # Process data
    print(color_text("Processing...", fg=YELLOW))
    # ... your code here ...
    print(color_text("Complete!", fg=GREEN, style=BOLD))

    # Get user input
    choice = footerMenu("Options: [1-9] Select | [Q] Quit")

    if choice == 'q':
        write_log("Application exited")
        print(color_text("Goodbye!", fg=GREEN))

if __name__ == "__main__":
    main()
```

## Next Steps

- Check out `example.py` for a complete demonstration
- Read the full [README.md](README.md) for detailed API documentation
- Explore the source code in the `CB9Lib/` directory

## Troubleshooting

### Colors not showing?

The library automatically detects if the terminal supports colors. If colors aren't showing:

```python
from CB9Lib import enable_colors

# Force enable colors
enable_colors(True)

# Or disable if needed
enable_colors(False)
```

### Import errors?

Make sure the library is installed:

```bash
pip show CB9Lib
```

If not installed, run:

```bash
pip install -e .
```

## Getting Help

- Check the [README.md](README.md) for full documentation
- Look at [example.py](example.py) for working examples
- Review the source code for detailed implementation
