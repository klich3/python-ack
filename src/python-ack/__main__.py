"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
__init__.py (c) 2024 
Created:  2024-01-02 17:37:05 
Desc: Inilization of RocketStore
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
        print("ok")
        pass
