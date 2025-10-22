# Claude Code Instructions for CB9Lib

## Quick Start for New Sessions

At the start of each session, Claude should:

1. **Read the preferences file first:**
   ```
   Read: .claude/preferences.md
   ```

2. **Understand the project context:**
   - This is a Python utility library for CLI applications
   - Focuses on terminal colors, UI components, file operations
   - Designed for simplicity and ease of use

3. **Follow the coding preferences:**
   - Use `from CB9Lib import *` import style
   - Left-align headers (don't center)
   - Use minimal prompts (`>` instead of verbose text)
   - Include type hints

## Common Tasks

### When Adding New Functions

1. Add to appropriate module (colors.py, func.py, or globals.py)
2. Include type hints
3. Add docstring
4. Update the `__init__.py` exports in `__all__`
5. Update function list in file header comments
6. Test with `pip install -e .`
7. Update README.md API reference if significant

### When Making Changes

1. Always validate syntax and logic
2. Test imports work: `python3 -c "from CB9Lib import *"`
3. Run example.py to verify: `python3 example.py`
4. Check type annotations are correct

### When Creating Examples

- Use the simple import style: `from CB9Lib import *`
- Follow the minimal UI aesthetic
- Demonstrate practical use cases

## File Structure Quick Reference

- `CB9Lib/__init__.py` - Package exports and version
- `CB9Lib/colors.py` - ANSI color system
- `CB9Lib/func.py` - UI and utility functions
- `CB9Lib/globals.py` - Global constants and paths
- `setup.py` - Package configuration (legacy)
- `pyproject.toml` - Modern packaging config
- `example.py` - Working demonstration
- `README.md` - Full documentation
- `QUICKSTART.md` - Quick start guide

## How to Load Preferences

### Method 1: Direct Instruction
User says: "Read my preferences" → Read `.claude/preferences.md`

### Method 2: Project Context
When user asks to work on CB9Lib, check for `.claude/preferences.md`

### Method 3: Explicit Request
User provides path: `.claude/preferences.md`

## Validation Checklist

When user asks to validate changes:
- [ ] Syntax is correct (no errors)
- [ ] Type annotations match usage
- [ ] Logic is sound (no type mismatches)
- [ ] Follows project preferences
- [ ] Imports work correctly
- [ ] Functions are exported in `__all__` if needed

## Remember

- User prefers minimal, clean code
- User prefers simple imports over explicit lists
- User values validation and testing
- Library should remain dependency-free
