#!/usr/bin/env python3
"""
Example usage of CB9Lib library
"""

from CB9Lib import *

def main():
    # Display application header
    header("CB9Lib Demo", "v1.2")

    # Show some colored text
    print(color_text("Welcome to CB9Lib!", fg=CYAN, style=BOLD))
    print(color_text("This library provides:", fg=GREEN))
    print(color_text("  ✓ Terminal colors and styles", fg=YELLOW))
    print(color_text("  ✓ UI components for CLI apps", fg=YELLOW))
    print(color_text("  ✓ File and JSON utilities", fg=YELLOW))
    print(color_text("  ✓ Logging functionality", fg=YELLOW))
    print()

    # Create a banner
    banner("Color Demonstration", fg=MAGENTA)

    # Test colors
    test_colors()

    # Demonstrate file operations
    print()
    banner("File Operations", fg=BLUE)

    # Create a sample config
    config = {
        "app_name": "CB9Lib Demo",
        "version": "1.1.0",
        "settings": {
            "color_enabled": True,
            "log_level": "INFO"
        }
    }

    # Save config
    save_json_config("demo_config.json", config)

    # Load config back
    loaded_config = load_json_config("demo_config.json")
    print(color_text(f"Loaded config: {loaded_config['app_name']}", fg=GREEN))


    # Log something
    SCRIPT_NAME="example.py"
    VERSION="v1.0"
    LOGFILE="/Users/john-ash/Documents/logs/example.log"
    log_header(SCRIPT_NAME, VERSION, LOGFILE)
    write_log("Demo application started successfully")

    print()
    # Show footer menu (commented out to not wait for input in demo)
    # choice = footerMenu("Demo Menu - Try the navigation!")
    # print(color_text(f"You selected: {choice}", fg=CYAN))

    print(color_text("\nDemo complete! Check demo_config.json and logs/ folder.", fg=GREEN, style=BOLD))

if __name__ == "__main__":
    main()
