#!/usr/bin/env python3
"""
Setup script for Day Supply National - Prescription Data Extractor
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="day-supply-national",
    version="2.0.0",
    author="Day Supply National Team",
    author_email="support@daysupplynational.com",
    description="A comprehensive prescription data extraction and standardization system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daysupplynational/prescription-extractor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "day_supply_national": ["data/*.csv"],
    },
    entry_points={
        "console_scripts": [
            "day-supply-extractor=day_supply_national.cli:main",
            "day-supply-demo=day_supply_national.demo:main",
            "day-supply-test=day_supply_national.test_suite:main",
        ],
    },
    keywords="pharmacy prescription healthcare day-supply medication",
    project_urls={
        "Bug Reports": "https://github.com/daysupplynational/prescription-extractor/issues",
        "Source": "https://github.com/daysupplynational/prescription-extractor",
        "Documentation": "https://github.com/daysupplynational/prescription-extractor/wiki",
    },
)
