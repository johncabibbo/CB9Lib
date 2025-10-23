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

### CB9Lib Module Header Requirements

**CRITICAL RULE for CB9Lib Package Updates:** When updating any module in the CB9Lib package (colors.py, func.py, globals.py, __init__.py), the header MUST follow these comprehensive documentation requirements:

#### Function List Format Requirements:
1. **Complete function signatures** with all parameters, defaults, and return types
2. **Function description** on indented line immediately below signature
3. **All arguments documented** one per line with descriptions
4. **Path type specifications** for file/folder arguments (absolute or relative)
5. **Example inputs** for all file/folder path parameters
6. **Return types** explicitly shown in signature (-> type)

#### Example Header Format for func.py:
```python
#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: func.py
# Project: Shared Library
# Version: 1.2
# Description: Common functions for Cloud Box 9 projects (UI + JSON + Console).
# Maintainer: Cloud Box 9 Inc.
# Last Modified Date: 2025-10-23
# -----------------------------------------------------------------------------
# Function List:
# -----------------------------------------------------------------------------
# function_name(param1: str, param2: int = 0) -> ReturnType
#     Brief description of what the function does
#     param1: Description of first parameter
#     param2: Description of second parameter
#
# file_operation(path: str) -> bool
#     Check if a file exists
#     path: Path to file (absolute or relative)
#           Example: "data.txt" or "/Users/user/data.txt"
#
# -----------------------------------------------------------------------------
# Revision History:
# -----------------------------------------------------------------------------
# v1.2 (2025-10-23)
#   • Description of changes
# -----------------------------------------------------------------------------
```

#### When to Update:
- Adding new functions → Add to Function List with complete documentation
- Modifying function signatures → Update the Function List entry
- Changing behavior → Update description and revision history
- Updating version → Increment version number and add revision history entry
- **Always** update Last Modified Date to current date

#### Validation Checklist for CB9Lib Module Headers:
- [ ] All functions listed in Function List section
- [ ] Each function has signature with all parameters and return type
- [ ] Each function has description line
- [ ] Each parameter documented with description
- [ ] File/folder paths show "absolute or relative"
- [ ] File/folder paths include example input
- [ ] Version number incremented if changes made
- [ ] Last Modified Date is current
- [ ] Revision History updated with changes

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

## User Defined Commands

This section contains custom commands that trigger specific actions. Add new commands here as needed.

**General Rules:**
- All shortcuts are **case insensitive** (e.g., "shortcuts", "SHORTCUTS", "Shortcuts" all work)
- Display shortcuts in **UPPERCASE** when showing them to the user
- Example: User types "export rules" → Display as "EXPORT RULES"

**Screenshot Reference Rule:**
- When user says "latest screenshot" or references a screenshot without a specific path:
  - Look in `/Users/john-ash/Documents/screenshotsLocal/`
  - Find the most recent image file (by modification time)
  - Read and analyze that file
  - Common image formats: .png, .jpg, .jpeg, .gif, .webp

---

### Command: "Export Rules"

**Trigger:** User says "Export Rules"

**Action:**
1. Generate the human-readable CB9Lib Module Header Requirements
2. Ensure `~/Documents/script/chatlog/` directory exists (create if needed)
3. Write the formatted rules to file using the specified header format
4. Confirm to user that the file has been written

**Output Location:** `/Users/john-ash/Documents/script/chatlog/claude1Rules.txt`

**Output Format:** Human-readable markdown format including:
- **Shortcuts list section** (at top) - All user-defined commands
- When rules apply
- The 6 core requirements with examples
- Full example
- When to update table
- Quick validation checklist
- Header structure template

**Header Format:**
- Main title: 90 dashes
  ```
  # ------------------------------------------------------------------------------------------
  # Title Text
  # ------------------------------------------------------------------------------------------
  ```
- Major sections (##): 60 dashes
  ```
  # ------------------------------------------------------------
  ## Section Name
  # ------------------------------------------------------------
  ```
- Subsections (###): 55 dashes
  ```
  # -------------------------------------------------------
  ### Subsection Name
  # -------------------------------------------------------
  ```
- Sub-subsections (####): 50 dashes (and continue decreasing by 5)
  ```
  # --------------------------------------------------
  #### Sub-subsection Name
  # --------------------------------------------------
  ```
- Minimum dash length: 30 dashes (for deepest nested sections)
- Use `#` comment character at start of border lines
- Markdown headers (##, ###, ####) for section titles

---

### Command: "shortcuts"

**Trigger:** User says "shortcuts"

**Action:**
1. Display a list of all defined user commands from this section
2. Show the trigger phrase and brief description for each command
3. Format as a readable table or list

**Output Format:** Console output showing:
- Command name/trigger
- Brief description of what it does
- Output location (if applicable)

**Example Output:**
```
User Defined Commands:
----------------------
1. "Export Rules"
   - Exports CB9Lib Module Header Documentation Rules
   - Output: ~/Documents/script/chatlog/claude1Rules.txt

2. "shortcuts"
   - Displays this list of available commands
```

---

### Command: "commit and push"

**Trigger:** User says "commit and push" (case insensitive)

**Action:**
1. Check git status to see all modified/untracked files
2. Read current version from `CB9Lib/__init__.py` (__version__)
3. Display current repository name
4. Stage all relevant changes (add files to git)
5. If multiple git repositories are detected in the working directories:
   - Display a menu with options:
     ```
     Select repository:
     Option A: >>> /path/to/repo1
     Option B: >>> /path/to/repo2
     ```
   - Wait for user selection
6. Generate appropriate commit message based on changes
7. Include version number in commit message (e.g., "v1.2.0" or similar format)
8. Create commit with generated message including version
9. Push to remote repository
10. Display repository name in confirmation
11. Confirm success with commit hash and push status

**Notes:**
- Follows standard git commit message conventions
- Displays repository name when performing commit and push
- Includes current version number in commit message
- Includes Claude Code co-authorship footer
- Checks for multiple repos in working directories
- Menu format uses "Option A: >>>" style
- Will not commit files that likely contain secrets (.env, credentials, etc.)

---

### Command: "Display N chats"

**Trigger:** User says "Display N chats" (where N is a number, e.g., "Display 5 chats", "Display 10 chats")

**Action:**
1. Extract the number N from the command
2. Retrieve the last N user commands/messages from the conversation history
3. Display them in a numbered list format with clear separation
4. Show commands only (not Claude's responses)

**Output Format:**
```
Last N Commands:
================
1. [command text]
2. [command text]
3. [command text]
...
N. [command text]
```

**Notes:**
- If N is not specified, default to last 5 commands
- Shows user input only, not assistant responses
- Numbered in chronological order (oldest to newest)
- Clear visual separation between entries

---

### Command: "Ready project"

**Trigger:** User says "Ready project"

**Action:**
1. Increment the version number by 0.1 (e.g., 1.2 → 1.3)
2. Update version in all appropriate files:
   - `CB9Lib/__init__.py` (__version__)
   - `setup.py` (version)
   - `pyproject.toml` (version)
   - Module headers that changed (func.py, colors.py, globals.py)
3. Update "Last Modified Date" to today's date in all changed module headers
4. Add entry to Revision History in changed modules
5. Display summary of version updates

**Notes:**
- Only updates headers for modules that have actual code changes
- Maintains consistent version numbering across all package files
- Updates Last Modified Date to current date (YYYY-MM-DD)

---

### Command: "Ready project version X"

**Trigger:** User says "Ready project version X" (where X is the new version number, e.g., "Ready project version 2.0", "Ready project version 1.5")

**Action:**
1. Set the version number to X (e.g., "Ready project version 2.0" sets version to 2.0)
2. Update version in all appropriate files:
   - `CB9Lib/__init__.py` (__version__)
   - `setup.py` (version)
   - `pyproject.toml` (version)
   - Module headers that changed (func.py, colors.py, globals.py)
3. Update "Last Modified Date" to today's date in all changed module headers
4. Add entry to Revision History in changed modules
5. Display summary of version updates

**Notes:**
- Sets version to specific value (not incremental)
- Only updates headers for modules that have actual code changes
- Maintains consistent version numbering across all package files
- Updates Last Modified Date to current date (YYYY-MM-DD)
- Example: "Ready project version 2.0" → version becomes 2.0

---

### Command: [Future Command Name]

**Trigger:** [User phrase or command]

**Action:**
[What should happen]

**Output Location:** [If applicable]

---

## Future Considerations

- Keep the library dependency-free (standard library only)
- Maintain backward compatibility for function signatures
- Test on macOS, Linux, and Windows for cross-platform compatibility
