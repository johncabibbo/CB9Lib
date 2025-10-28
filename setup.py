#!/usr/bin/env python3
#
# Filename: setup.py
# Project: CB9Lib
# Version: 1.3
# Description: Setup script for installing the Cloud Box 9 shared Python library.
# Maintainer: Cloud Box 9 Inc.
# Last Modified Date: 2025-10-25
# -----------------------------------------------------------------------------

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="CB9Lib",
    version="1.3.0",
    author="Cloud Box 9 Inc.",
    author_email="info@cloudbox9.com",
    description="Comprehensive utility library for Cloud Box 9 projects with terminal colors, interactive UI, logging, validation, and testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudbox9/CB9Lib",
    project_urls={
        "Bug Tracker": "https://github.com/cloudbox9/CB9Lib/issues",
        "Documentation": "https://github.com/cloudbox9/CB9Lib#readme",
        "Source Code": "https://github.com/cloudbox9/CB9Lib",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    keywords="terminal colors ansi cli ui utilities json logging validation testing tables menu",
    python_requires=">=3.10",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
        "images": [
            "Pillow>=10.0",  # Required for imgvid module
        ],
    },
    license="MIT",
)