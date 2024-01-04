"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
setup.py (c) 2024 
Created:  2024-01-03 02:40:06 
Desc: Setup for local installation development
"""

from setuptools import setup, find_packages

setup(
    name="python-ack",
    version="0.0.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Anton Sychev",
    author_email="anton@sychev.xyz",
    description="Python-ACK is a code-searching tool, similar to grep but optimized for programmers searching large trees of source code.",
    license="MIT",
    url="https://github.com/klich3/python-ack",
    entry_points={
        "console_scripts": [
            "python-ack = python_ack.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
