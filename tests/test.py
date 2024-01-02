"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
test.py (c) 2024 
Created:  2024-01-03 00:26:05 
Desc: test file
Docs: documentation
"""

import os
import sys

from python_ack.ack import ack

def main():
    print(os.getcwd())

    regex = 'apple'
    number_processes = 10
    search_binary = False
    use_ansi_colors = True
    exclude_path = []  # Puedes proporcionar una lista de exclusiones si es necesario

    my_ack_instance = ack(
        regex=regex,
        number_processes=number_processes,
        search_binary=search_binary,
        use_ansi_colors=use_ansi_colors,
        exclude_path=exclude_path,
    )
    my_ack_instance.search()  # Llama al método search después de la inicialización

if __name__ == "__main__":
    main()