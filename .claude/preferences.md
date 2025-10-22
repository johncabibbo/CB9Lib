# CB9Lib Project Preferences

**Important: Read this file at the start of each session to understand project preferences.**

## Code Style Preferences

### Import Style
- **Preference:** Use `from CB9Lib import *` style imports
- **Reason:** Library is designed for convenience; all exports are curated in `__all__`
- **Example:**
  ```python
  from CB9Lib import *
  # NOT: from CB9Lib import header, footer, color_text, RED, GREEN...
  ```

### Type Annotations
- **Use type hints** for all function parameters and return values
- **Format:** `def function_name(param: str, count: int = 0) -> bool:`

### UI Design Philosophy
- **Minimal and clean** - Prefer simple prompts over verbose text
- **Left-aligned headers** - Don't center titles (user preference)
- **Simple prompts** - Use `> ` instead of `Enter choice: `

### Width Handling
- **Default:** Auto-detect terminal width with `shutil.get_terminal_size().columns`
- **Override:** Support optional `width: int = 0` parameter where 0 = auto-detect

## Project Structure

```
CB9Lib/
├── CB9Lib/              # Main package directory
│   ├── __init__.py      # Package initialization with curated exports
│   ├── colors.py        # ANSI color system with TTY detection
│   ├── func.py          # UI, file, and utility functions
│   └── globals.py       # Global settings and constants
├── .claude/             # Claude Code preferences and commands
├── setup.py             # Package installation configuration
├── pyproject.toml       # Modern Python packaging configuration
├── README.md            # Full documentation
├── QUICKSTART.md        # Quick start guide
├── LICENSE              # MIT License
└── example.py           # Working example script
```

## Function Signature Standards

### Current Functions in func.py:
```python
# UI Functions
def header(title: str = "Untitled Script", version: str = "v1.0", width: int = 0)
def footerMenu(legend: str = "", width: int = 0) -> str

# Core Utilities
def clear_screen()
def pause(msg: str = "Press Enter to continue...")
def sleep(seconds: float = 1.0)

# JSON Helpers
def load_json_config(jsonFileName: str) -> dict
def save_json_config(jsonFileName: str, data: dict)

# File Utilities
def file_exists(path: str) -> bool
def folder_exists(path: str) -> bool
def ensure_folder(path: str)
def list_files(path: str, ext: str = None) -> list

# Logging
def write_log(message: str, filename: str = None)

# Testing
def test_ui()
```

## Documentation Standards

### File Headers

**CRITICAL RULE:** Every Python file MUST include Project and Version in the header. No exceptions.

**Header Validation Checklist:**
- [ ] Shebang on line 1
- [ ] `# =============` border on line 2
- [ ] **Filename:** field present
- [ ] **Project:** field present ✅ REQUIRED
- [ ] **Version:** field present ✅ REQUIRED
- [ ] **Description:** section present (or minimal comment)
- [ ] `# =============` closing border

**Standard Cloud Box 9 Python File Header Format:**

**Important:** Shebang is on line 1, then the comment header block starts on line 2.

```python
#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
# =============================================================================
# Filename: <filename>.py
# Project: <project_name>
# Version: <version>
# Last Modified Date: <YYYY-MM-DD>
# Category: <category> (e.g., Backup, Utilities, CLI, etc.)
# OS: Mac/Linux (or specific OS requirement)
# Maintainer: Cloud Box 9
# -----------------------------------------------------------------------------
# Description:
#   <Detailed description of what this file does>
#
#   Features:
#     • Feature 1
#     • Feature 2
#     • Feature 3
#
# Usage:
#   python3 <filename>.py [options]
#   python3 <filename>.py --help
#
# Notes:
#   • Important note 1
#   • Important note 2
# -----------------------------------------------------------------------------
# Revision History:
#   v<version> — <YYYY-MM-DD> — <description of changes>
#   v<version> — <YYYY-MM-DD> — <description of changes>
# =============================================================================

<imports go here>
```

**For library modules (like CB9Lib):**

```python
#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
# =============================================================================
# Filename: <filename>.py
# Project: CB9Lib
# Version: <version>
# Last Modified Date: <YYYY-MM-DD>
# Category: Library
# OS: Mac/Linux/Windows
# Maintainer: Cloud Box 9
# -----------------------------------------------------------------------------
# Description:
#   <Brief description of module purpose>
#
# Function List:
#   • function_one(param: type) -> return_type
#   • function_two(param: type)
#   • function_three()
#
# Notes:
#   • Implementation details
#   • Dependencies (if any)
# -----------------------------------------------------------------------------
# Revision History:
#   v<version> — <YYYY-MM-DD> — <description of changes>
# =============================================================================

<imports go here>
```

**For simple utility scripts:**

**Note:** Even simple scripts MUST have Project and Version fields.

```python
#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
# =============================================================================
# Filename: <filename>.py
# Project: <project_name>
# Version: <version>
# Last Modified Date: <YYYY-MM-DD>
# Maintainer: Cloud Box 9
# -----------------------------------------------------------------------------
# Description:
#   <Brief description>
# =============================================================================

<imports go here>
```

**Minimal acceptable header (still requires Project and Version):**

```python
#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
# =============================================================================
# Filename: <filename>.py
# Project: <project_name>
# Version: <version>
# =============================================================================

<imports go here>
```

**Example script with alternative docstring style:**

**Note:** If using docstring style, Project and Version can be in a module-level constant:

```python
#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
"""
Brief description of what this script does.
Can be multiple lines if needed.
"""

__project__ = "<project_name>"
__version__ = "<version>"

# Standard imports
import os
import sys

# Third-party imports (if any)

# Local imports
from CB9Lib import *

def main():
    # Script logic here
    pass

if __name__ == "__main__":
    main()
```

**However, the preferred method is the full comment header block shown above.**

### JSON File Headers

**CRITICAL RULE:** Every JSON configuration file MUST include metadata at the top level.

**Required Fields for All JSON Files:**
```json
{
  "_metadata": {
    "project": "<project_name>",
    "version": "<version>",
    "lastUpdated": "<YYYY-MM-DD>",
    "description": "<brief description of this config file>"
  },

  "your_config_data": "goes here"
}
```

**Alternative Format (metadata as top-level keys):**
```json
{
  "project": "<project_name>",
  "version": "<version>",
  "lastUpdated": "<YYYY-MM-DD>",

  "your_config_data": "goes here"
}
```

**Example - Configuration File:**
```json
{
  "_metadata": {
    "project": "CB9Lib",
    "version": "1.1.0",
    "lastUpdated": "2025-10-22",
    "description": "CB9Lib application configuration"
  },

  "database": {
    "host": "localhost",
    "port": 3306
  },
  "settings": {
    "debug": false,
    "logLevel": "INFO"
  }
}
```

**Example - Data File:**
```json
{
  "project": "BackupTool",
  "version": "1.8",
  "lastUpdated": "2025-10-14",

  "profiles": [
    {
      "id": "profile1",
      "name": "Production Backup"
    }
  ]
}
```

**Validation Checklist for JSON Files:**
- [ ] **project** field present ✅ REQUIRED
- [ ] **version** field present ✅ REQUIRED
- [ ] **lastUpdated** field present ✅ REQUIRED (format: YYYY-MM-DD)
- [ ] Valid JSON syntax
- [ ] Proper indentation (2 or 4 spaces)

### Docstrings
- Use brief, descriptive docstrings for all functions
- Format: `"""Brief description of what the function does."""`
- For complex functions, add parameter and return descriptions:
  ```python
  def complex_function(param1: str, param2: int = 0) -> dict:
      """
      Brief description of function.

      Args:
          param1: Description of param1
          param2: Description of param2 (default: 0)

      Returns:
          dict: Description of return value
      """
  ```

## Git Workflow

### Commit Style
- Use conventional commits when possible
- Example: `feat: add width parameter to header and footerMenu`

### Files to Ignore
- See `.gitignore` for complete list
- Key ones: `__pycache__/`, `*.egg-info/`, `dist/`, `build/`, `.DS_Store`

## Testing Philosophy

- Test with `pip install -e .` for development
- Run `example.py` to verify basic functionality
- Test color output in actual terminal (not redirected)

## Color System Notes

- **Auto-detection:** Colors automatically disabled when output is piped/redirected
- **Manual control:** Use `enable_colors(True/False)` to override
- **TTY detection:** Uses `sys.stdout.isatty()` for smart detection

## Common Patterns

### Creating a CLI Application
```python
from CB9Lib import *

def main():
    header("My App", "v1.0")
    banner("Section Title", fg=CYAN)
    print(color_text("Status message", fg=GREEN))
    choice = footerMenu("Menu legend")

if __name__ == "__main__":
    main()
```

### File Operations
```python
from CB9Lib import *

ensure_folder("logs")
config = load_json_config("config.json")
write_log("Application started")
```

## Version Information

- **Current Version:** 1.1.0
- **Python Requirement:** >= 3.10
- **Dependencies:** None (uses only standard library)

## Future Considerations

- Keep the library dependency-free (standard library only)
- Maintain backward compatibility for function signatures
- Test on macOS, Linux, and Windows for cross-platform compatibility
