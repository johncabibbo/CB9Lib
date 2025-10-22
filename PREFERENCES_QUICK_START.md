# 🚀 CB9Lib Preferences Quick Start

## TL;DR - How to Use This in Future Sessions

### At the Start of Your Next Session, Just Say:

```
Read .claude/preferences.md
```

That's it! Claude will load all your project preferences and coding standards.

---

## What's Included

Your preferences are stored in `.claude/preferences.md` and include:

✅ Import style (`from CB9Lib import *`)
✅ Type annotation requirements
✅ UI design philosophy (minimal, clean)
✅ Function signatures and standards
✅ Documentation format
✅ Common code patterns
✅ Testing approach

---

## Files Created

```
.claude/
├── preferences.md      ← Your coding standards (MAIN FILE)
├── README.md          ← Instructions for Claude
└── HOW_TO_USE.md      ← Detailed guide for you
```

---

## Example Usage

### Scenario 1: Adding a New Function
```
You: "Read my preferences, then add a confirm() function to CB9Lib"
Claude: [Reads preferences] [Adds function with proper style]
```

### Scenario 2: Validating Changes
```
You: "I updated colors.py. Read preferences and validate my changes."
Claude: [Checks against your standards]
```

### Scenario 3: Creating Examples
```
You: "Create an example script. Use my preferences."
Claude: [Uses preferred import style and patterns]
```

---

## Key Preferences Summary

| Aspect | Your Preference |
|--------|----------------|
| **Imports** | `from CB9Lib import *` |
| **Type Hints** | Required for all functions |
| **Header Style** | Left-aligned (not centered) |
| **Prompts** | Minimal (`>` not `Enter choice:`) |
| **Width** | Auto-detect with optional override |
| **Dependencies** | None (stdlib only) |

---

## Updating Preferences

Edit `.claude/preferences.md` anytime to:
- Add new standards
- Update existing preferences
- Document new patterns
- Add project-specific rules

---

## Remember

Claude **cannot** remember between sessions, but it **can** read this file!

So always start with: **"Read .claude/preferences.md"**

---

For more details, see `.claude/HOW_TO_USE.md`
