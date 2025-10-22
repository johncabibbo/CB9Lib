# How to Use Preferences in Future Sessions

## For You (The User)

### Starting a New Session

Simply tell Claude one of these:

**Option 1 - Direct:**
```
Read .claude/preferences.md
```

**Option 2 - Context-based:**
```
Load my project preferences
```

**Option 3 - In your request:**
```
I need to add a new function to CB9Lib. Check my preferences first.
```

### What's Included

Your preferences file contains:

✅ **Code Style**
- Import style: `from CB9Lib import *`
- Type hints required
- UI design philosophy (minimal, clean)

✅ **Project Structure**
- Directory layout
- File purposes
- Function signatures

✅ **Documentation Standards**
- File header format
- Docstring style

✅ **Common Patterns**
- Example code templates
- Best practices

✅ **Testing Approach**
- How to validate changes
- Test commands

## Quick Commands for Claude

Here are shortcuts you can use:

| What You Say | What Claude Does |
|--------------|------------------|
| "Read my preferences" | Reads `.claude/preferences.md` |
| "Validate my changes" | Checks syntax, types, logic, runs tests |
| "Add function X to CB9Lib" | Reads preferences, adds function with proper style |
| "Update the docs" | Updates README.md and QUICKSTART.md |

## Files in .claude/

- **preferences.md** - Your coding preferences and project standards
- **README.md** - Instructions for Claude on how to work with this project
- **HOW_TO_USE.md** - This file! Instructions for you

## Example Session Start

```
You: "I want to add a new prompt() function to CB9Lib. Read my preferences first."

Claude: [Reads .claude/preferences.md]
        [Understands: use type hints, minimal style, update __all__, etc.]
        [Proposes implementation following your standards]
```

## Updating Preferences

Edit `.claude/preferences.md` anytime to add:
- New coding standards
- Project-specific patterns
- Function naming conventions
- Any other preferences

Claude will use the updated preferences in the next session when you ask it to read the file.

## Pro Tips

1. **Be specific:** "Read preferences and validate my changes to func.py"
2. **Reference it early:** Mention it at the start of the session
3. **Update regularly:** Keep preferences.md current with your evolving standards
4. **Use it for validation:** "Does this follow my preferences?"

## What's NOT Saved

Remember, Claude won't remember:
- Previous conversation history
- What you worked on last time
- Temporary decisions made during a session

That's why the preferences file is valuable - it persists your standards across sessions!
