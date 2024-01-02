"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
setup.py (c) 2024 
Created:  2024-01-03 02:40:06 
Desc: setup for local installation development
Docs: documentation
"""

from setuptools import setup, find_packages

setup(
    name='python-ack',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
)