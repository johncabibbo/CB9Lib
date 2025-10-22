# How to Edit Your Preferences

## Quick Guide: Adding New Preferences

### Step 1: Open the Preferences File

Edit `.claude/preferences.md` in any text editor:

```bash
# Using your favorite editor
nano .claude/preferences.md
# or
vim .claude/preferences.md
# or
code .claude/preferences.md
```

### Step 2: Find the Right Section

The preferences file is organized into sections:

- **Code Style Preferences** - Import style, type hints, UI philosophy
- **Project Structure** - Directory layout
- **Function Signature Standards** - Function definitions
- **Documentation Standards** - File headers, docstrings ⭐ (We just edited this!)
- **Git Workflow** - Commit style, files to ignore
- **Testing Philosophy** - Testing approach
- **Common Patterns** - Code templates

### Step 3: Add Your Content

Use the existing format as a template. For example:

**Example 1: Adding a New Code Style Rule**

```markdown
### Variable Naming
- **Preference:** Use snake_case for variables and functions
- **Constants:** Use UPPER_CASE for constants
- **Example:**
  ```python
  user_name = "John"  # Good
  MAX_RETRIES = 3     # Good
  userName = "John"   # Bad
  ```
```

**Example 2: Adding a New Template**

```markdown
### Test File Template

```python
#!/usr/bin/env python3
#
# Filename: test_<module>.py
# Project: CB9Lib Tests
# Description: Unit tests for <module>
# -----------------------------------------------------------------------------

import pytest
from CB9Lib import *

def test_function_name():
    """Test description."""
    assert True
```
```

**Example 3: Adding Project-Specific Rules**

```markdown
### Database Conventions
- **Connection Pooling:** Always use connection pools
- **Transactions:** Wrap multi-step operations in transactions
- **Error Handling:** Log all database errors to error.log
```

## What I Just Added

I expanded the **Documentation Standards** section with:

✅ **Standard Python File Header** - Basic template
✅ **Module Header with Function List** - For files with multiple functions
✅ **Header with Revision History** - For tracking changes
✅ **Example Script Header** - For standalone scripts
✅ **Enhanced Docstring Format** - Including Args/Returns documentation

Now when you start a new session and say "Read .claude/preferences.md", Claude will know exactly what file header format to use!

## Common Things to Add

### Code Formatting
```markdown
### Line Length
- **Maximum:** 100 characters per line
- **Exceptions:** Long URLs, import statements
```

### Error Handling
```markdown
### Error Handling Standards
- Always catch specific exceptions, not generic `Exception`
- Log errors with `write_log()` before raising
- Use try-except-finally for resource cleanup
```

### Testing Requirements
```markdown
### Test Coverage
- **Minimum:** 80% code coverage
- **Required tests:** All public functions must have tests
- **Test naming:** test_<function_name>_<scenario>
```

### Naming Conventions
```markdown
### File Naming
- **Python modules:** lowercase_with_underscores.py
- **Test files:** test_<module_name>.py
- **Examples:** example_<feature>.py
```

## Tips

1. **Be Specific:** Include examples whenever possible
2. **Use Sections:** Keep it organized with headers
3. **Add "Why":** Explain reasons for preferences
4. **Keep Updated:** Update when your standards evolve
5. **Reference Files:** Point to existing code as examples

## Testing Your Changes

After editing preferences, test it in a new session:

```
You: "Read .claude/preferences.md and create a new file called utils.py with proper headers"

Claude: [Reads updated preferences] [Creates file with your header format]
```

## File Structure Reference

```
.claude/
├── preferences.md          ← YOUR MAIN FILE - Edit this!
├── README.md              ← Instructions for Claude
├── HOW_TO_USE.md          ← How to use preferences
└── EDITING_PREFERENCES.md ← This file!
```

## Example: What You Might Add Next

Maybe you want to add a preference for how to handle configuration files:

```markdown
### Configuration File Standards

**Config File Naming:**
- Development: `config.dev.json`
- Production: `config.prod.json`
- Local overrides: `config.local.json` (gitignored)

**Required Config Keys:**
```json
{
    "app_name": "string",
    "version": "string",
    "environment": "dev|prod|test",
    "log_level": "DEBUG|INFO|WARN|ERROR"
}
```

**Loading Pattern:**
```python
from CB9Lib import load_json_config

config = load_json_config("config.json")
app_name = config.get("app_name", "Default App")
```
```

Just add sections like this to `.claude/preferences.md`!
