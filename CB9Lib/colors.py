#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
#
# Filename: colors.py
# Project: Shared Library
# Version: 1.2
# Description: Full ANSI color and style system with terminal detection.
# Maintainer: Cloud Box 9 Inc.
# Last Modified Date: 2025-10-22
# -----------------------------------------------------------------------------
# 
# Example:
# 
# from lib.colors import *
# 
# banner("Color Test: AUTO + MANUAL Toggle")
# 
# print(color_text("Info: System running normally.", fg=GREEN))
# print(color_text("Warning: Low disk space.", fg=YELLOW, style=BOLD))
# print(color_text("Error: Sync failed!", fg=RED, bg=BG_BRIGHT_BLACK))
# 
# # Manual override
# enable_colors(False)
# print(color_text("This line will have no color.", fg=RED))
# 
# enable_colors(True)
# print(color_text("Colors re-enabled!", fg=BRIGHT_CYAN))
# 
# -----------------------------------------------------------------------------
# Formatting and Colors
#
# Category				Range		Example
# Foreground			30–37		\033[31m = red
# Background			40–47		\033[44m = blue bg
# Bright Foreground		90–97		\033[93m = bright yellow
# Bright Background		100–107		\033[103m = bright yellow bg
# Extended				0–255		\033[38;5;123m
# True Color			RGB 		\033[38;2;255;0;255m
# 
# -----------------------------------------------------------------------------

import sys

# -----------------------------------------------------------------------------
# AUTO COLOR DETECTION
# -----------------------------------------------------------------------------
# Automatically disable color when output is redirected to a file or pipe.
# You can override this behavior by changing AUTO_COLOR manually.
AUTO_COLOR = True   # Default: colors ON
FORCE_COLOR = True  # Manual toggle flag (can be changed in runtime)

def _is_tty():
    """Check if the output stream supports colors (TTY)."""
    return sys.stdout.isatty()

def _color_enabled():
    """Return True if color should be active."""
    return AUTO_COLOR and FORCE_COLOR and _is_tty()

# -----------------------------------------------------------------------------
# INTERNAL HELPER
# -----------------------------------------------------------------------------
def _ansi(code: str) -> str:
    """Return ANSI code only if color is active."""
    return code if _color_enabled() else ""

# -----------------------------------------------------------------------------
# Base Control Codes
# -----------------------------------------------------------------------------
ESC = "\033"
RESET = _ansi(f"{ESC}[0m")
BOLD = _ansi(f"{ESC}[1m")
DIM = _ansi(f"{ESC}[2m")
ITALIC = _ansi(f"{ESC}[3m")
UNDERLINE = _ansi(f"{ESC}[4m")
BLINK = _ansi(f"{ESC}[5m")
INVERSE = _ansi(f"{ESC}[7m")
HIDDEN = _ansi(f"{ESC}[8m")
STRIKE = _ansi(f"{ESC}[9m")

# -----------------------------------------------------------------------------
# Standard Colors
# -----------------------------------------------------------------------------
BLACK   = _ansi(f"{ESC}[30m")
RED     = _ansi(f"{ESC}[31m")
GREEN   = _ansi(f"{ESC}[32m")
YELLOW  = _ansi(f"{ESC}[33m")
BLUE    = _ansi(f"{ESC}[34m")
MAGENTA = _ansi(f"{ESC}[35m")
CYAN    = _ansi(f"{ESC}[36m")
WHITE   = _ansi(f"{ESC}[37m")

# -----------------------------------------------------------------------------
# Bright Colors
# -----------------------------------------------------------------------------
BRIGHT_BLACK   = _ansi(f"{ESC}[90m")
BRIGHT_RED     = _ansi(f"{ESC}[91m")
BRIGHT_GREEN   = _ansi(f"{ESC}[92m")
BRIGHT_YELLOW  = _ansi(f"{ESC}[93m")
BRIGHT_BLUE    = _ansi(f"{ESC}[94m")
BRIGHT_MAGENTA = _ansi(f"{ESC}[95m")
BRIGHT_CYAN    = _ansi(f"{ESC}[96m")
BRIGHT_WHITE   = _ansi(f"{ESC}[97m")

# -----------------------------------------------------------------------------
# Background Colors
# -----------------------------------------------------------------------------
BG_BLACK   = _ansi(f"{ESC}[40m")
BG_RED     = _ansi(f"{ESC}[41m")
BG_GREEN   = _ansi(f"{ESC}[42m")
BG_YELLOW  = _ansi(f"{ESC}[43m")
BG_BLUE    = _ansi(f"{ESC}[44m")
BG_MAGENTA = _ansi(f"{ESC}[45m")
BG_CYAN    = _ansi(f"{ESC}[46m")
BG_WHITE   = _ansi(f"{ESC}[47m")

# -----------------------------------------------------------------------------
# Bright Background Colors
# -----------------------------------------------------------------------------
BG_BRIGHT_BLACK   = _ansi(f"{ESC}[100m")
BG_BRIGHT_RED     = _ansi(f"{ESC}[101m")
BG_BRIGHT_GREEN   = _ansi(f"{ESC}[102m")
BG_BRIGHT_YELLOW  = _ansi(f"{ESC}[103m")
BG_BRIGHT_BLUE    = _ansi(f"{ESC}[104m")
BG_BRIGHT_MAGENTA = _ansi(f"{ESC}[105m")
BG_BRIGHT_CYAN    = _ansi(f"{ESC}[106m")
BG_BRIGHT_WHITE   = _ansi(f"{ESC}[107m")

# -----------------------------------------------------------------------------
# 256 and RGB Colors
# -----------------------------------------------------------------------------
def color256(code: int) -> str:
    return _ansi(f"{ESC}[38;5;{code}m")

def bg256(code: int) -> str:
    return _ansi(f"{ESC}[48;5;{code}m")

def rgb(r: int, g: int, b: int) -> str:
    return _ansi(f"{ESC}[38;2;{r};{g};{b}m")

def bg_rgb(r: int, g: int, b: int) -> str:
    return _ansi(f"{ESC}[48;2;{r};{g};{b}m")

# -----------------------------------------------------------------------------
# User Functions
# -----------------------------------------------------------------------------
def enable_colors(state: bool = True):
    """
    Manually toggle color output.
    Example:
        enable_colors(False)  # disable even if TTY
    """
    global FORCE_COLOR
    FORCE_COLOR = state

def color_text(text: str, fg: str = "", bg: str = "", style: str = "") -> str:
    """Apply color/style safely."""
    return f"{style}{fg}{bg}{text}{RESET}"

def banner(text: str, fg=CYAN, style=BOLD):
    """Print a banner safely."""
    line = "-" * 60
    print(f"{style}{fg}{line}\n{text.center(60)}\n{line}{RESET}")

def test_colors():
    """Show color preview (only works if colors enabled)."""
    banner("Standard Colors")
    for name, val in {
        "BLACK": BLACK, "RED": RED, "GREEN": GREEN, "YELLOW": YELLOW,
        "BLUE": BLUE, "MAGENTA": MAGENTA, "CYAN": CYAN, "WHITE": WHITE
    }.items():
        print(f"{val}{name}{RESET} ", end="")
    print("\n")

    banner("Bright Colors")
    for name, val in {
        "BRIGHT_BLACK": BRIGHT_BLACK, "BRIGHT_RED": BRIGHT_RED,
        "BRIGHT_GREEN": BRIGHT_GREEN, "BRIGHT_YELLOW": BRIGHT_YELLOW,
        "BRIGHT_BLUE": BRIGHT_BLUE, "BRIGHT_MAGENTA": BRIGHT_MAGENTA,
        "BRIGHT_CYAN": BRIGHT_CYAN, "BRIGHT_WHITE": BRIGHT_WHITE
    }.items():
        print(f"{val}{name}{RESET} ", end="")
    print("\n")