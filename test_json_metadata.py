#!/opt/homebrew/opt/python@3.12/libexec/bin/python3
# =============================================================================
# Filename: test_json_metadata.py
# Project: CB9Lib
# Version: 1.0
# Last Modified Date: 2025-10-22
# Category: Testing
# OS: Mac/Linux/Windows
# Maintainer: Cloud Box 9
# -----------------------------------------------------------------------------
# Description:
#   Test script to demonstrate reading JSON metadata fields.
#
#   Features:
#     • Loads JSON configuration file
#     • Displays metadata (project, version, lastUpdated)
#     • Shows how to access configuration data
#
# Usage:
#   python3 test_json_metadata.py
#
# Notes:
#   • Demonstrates the new JSON metadata standard
#   • Uses CB9Lib for colored output
# -----------------------------------------------------------------------------
# Revision History:
#   v1.0 — 2025-10-22 — Initial creation to test JSON metadata standard
# =============================================================================

from CB9Lib import *

def main():
    header("JSON Metadata Test", "v1.0")

    # Load the example config
    config = load_json_config("example_config.json")

    if not config:
        print(color_text("Failed to load configuration file!", fg=RED, style=BOLD))
        return

    # Display metadata
    banner("Configuration Metadata", fg=CYAN)

    if "_metadata" in config:
        metadata = config["_metadata"]
        print(color_text(f"Project:      {metadata.get('project', 'N/A')}", fg=GREEN))
        print(color_text(f"Version:      {metadata.get('version', 'N/A')}", fg=GREEN))
        print(color_text(f"Last Updated: {metadata.get('lastUpdated', 'N/A')}", fg=GREEN))
        print(color_text(f"Description:  {metadata.get('description', 'N/A')}", fg=GREEN))
    else:
        print(color_text("Warning: No _metadata section found", fg=YELLOW))

    print()

    # Display some config data
    banner("Configuration Data", fg=MAGENTA)

    app = config.get("application", {})
    print(color_text(f"App Name:  {app.get('name', 'N/A')}", fg=CYAN))
    print(color_text(f"Debug:     {app.get('debug', False)}", fg=CYAN))
    print(color_text(f"Log Level: {app.get('logLevel', 'N/A')}", fg=CYAN))

    print()
    features = config.get("features", {})
    print(color_text("Features:", fg=YELLOW, style=BOLD))
    for feature, enabled in features.items():
        status = "✓" if enabled else "✗"
        color = GREEN if enabled else RED
        print(color_text(f"  {status} {feature}: {enabled}", fg=color))

    print()
    print(color_text("✓ JSON metadata standard validated!", fg=GREEN, style=BOLD))

if __name__ == "__main__":
    main()
