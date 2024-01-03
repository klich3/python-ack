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
    folder = os.path.join(os.getcwd(), "tests", "crw")

    instance = ack(
        path=folder,
        regexp="apple",
        # exclude_regexp=["solor"],
        num_procesos=10,
        # exclude_paths_regexp=["exclude_*"],
        follow_links=False,
        # use_ansi_colors=False,
        # search_function=None, #TODO: test
        # return_as_dict=True,
    )
    instance.process_folders()
    result = instance.print_result()

    print(result)

    duration = instance.get_duration()
    if duration is not None:
        print(f"\nComplete in {duration}ms.")


if __name__ == "__main__":
    main()
