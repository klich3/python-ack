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
        regex,
        number_processes=10,
        search_binary=False,
        use_ansi_colors=True,
        exclude_path=[],
    ):
        print("Clase ack inicializada.")
        self.regex = regex
        self.number_processes = number_processes
        self.search_binary = search_binary
        self.use_ansi_colors = use_ansi_colors
        self.exclude_path = exclude_path or []

    def search(self):
        # Realizar operaciones de búsqueda aquí
        pass



