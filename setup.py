"""
This module contains the setup configuration for the VoLTGoLD-YT package.
"""

from setuptools import find_packages, setup
from pyutube.utils import __version__

# Read the README file to use as the long description
with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    # 🔹 اسم الحزمة (اسم الفورك)
    name="VoLTGoLD-YT",

    version=__version__,

    # 🔹 بياناتك
    author="VOLT5775",
    author_email="VOLT5775@users.noreply.github.com",

    description=(
        "High performance CLI YouTube downloader "
        "(video / audio / shorts / playlists) "
        "with smart caching and auto quality handling"
    ),

    long_description=description,
    long_description_content_type="text/markdown",

    keywords=[
        "youtube",
        "download",
        "cli",
        "pyutube",
        "voltgold",
        "yt-downloader",
        "pytubefix",
        "pytube",
        "youtube-dl",
    ],

    license="MIT",

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],

    include_package_data=True,

    python_requires=">=3.6",

    install_requires=[
        "pytubefix",
        "inquirer",
        "yaspin",
        "typer",
        "requests",
        "rich",
        "termcolor",
        "moviepy",
        "setuptools",
    ],

    entry_points={
        "console_scripts": [
            # 🔹 اسم الأمر في التيرمنال
            "gold=pyutube:cli.app",
        ],
    },

    project_urls={
        "Homepage": "https://github.com/VOLT5775/VoLTGoLD-YT",
        "Source Code": "https://github.com/VOLT5775/VoLTGoLD-YT",
        "Bug Tracker": "https://github.com/VOLT5775/VoLTGoLD-YT/issues",
        "Documentation": "https://github.com/VOLT5775/VoLTGoLD-YT",
        "Author": "https://github.com/VOLT5775",
    },

    platforms=["Linux", "Windows", "MacOS"],
    packages=find_packages(),
)