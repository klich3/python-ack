"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
ack.py (c) 2024 
Created:  2024-01-03 02:27:39 
Desc: ACK tool
Docs: documentation
"""

import re
import sys
import datetime
from subprocess import Popen
from collections import deque
from multiprocessing import Process


class ack:
    def __init__(
        self,
        folder_path,
        regex,
        number_processes=10,
        search_binary=False,
        use_ansi_colors=True,
        exclude_path=[],
    ):
        '''
        initialize ack instance
        @folder_path: path to folder to search
        @regex: regex to search
        @number_processes: number of processes to use
        @search_binary: search binary files
        @use_ansi_colors: use ansi colors
        @exclude_path: list of paths to exclude
        '''
        self.folder_path = folder_path
        self.regex = regex
        self.number_processes = number_processes
        self.search_binary = search_binary
        self.use_ansi_colors = use_ansi_colors
        self.exclude_path = exclude_path or []

    def search(self):
        # Realizar operaciones de búsqueda aquí
        pass



