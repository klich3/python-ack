"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
__init__.py (c) 2024 
Created:  2024-01-02 17:37:05 
Desc: Inilization of RocketStore
"""

import sys, os, argparse, re, datetime
from .ack import ack
from .__version__ import (
    __title__,
    __description__,
    __url__,
)


def main():
    parser = argparse.ArgumentParser(
        prog="python-ack",
        description=f"{__description__}",
        epilog="For more information visit %s" % __url__,
    )

    parser.add_argument(
        "pattern",
        metavar="PATTERN",
        action="store",
        help="Pattern to search for.",
    )

    parser.add_argument(
        "directory",
        metavar="DIRECTORY",
        nargs="?",
        default=os.getcwd(),
        help="A directory to search.",
    )

    parser.add_argument(
        "--num-processes",
        "-n",
        dest="num_processes",
        action="store",
        default=4,
        type=int,
        help="Number of processes to use.",
    )

    parser.add_argument(
        "--exclude-path",
        "-x",
        metavar="EXCLUDE_PATH_PATTERN",
        dest="exclude_paths_regexp",
        action="append",
        default=[],
        type=str,
        help="Exclude paths matching EXCLUDE_PATH_PATTERN.",
    )

    if sys.version_info >= (2, 6):
        parser.add_argument(
            "--follow-links",
            "-f",
            dest="follow_links",
            action="store_true",
            default=False,
            help="Follow symlinks (Python >= 2.6 only).",
        )

    parser.add_argument(
        "--exclude-search",
        "-s",
        metavar="EXCLUDE_PATTERN",
        dest="exclude_regexp",
        action="append",
        default=[],
        type=str,
        help="Exclude results matching EXCLUDE_PATTERN.",
    )

    parser.add_argument(
        "--no-colors",
        "-c",
        dest="use_ansi_colors",
        action="store_false",
        default=True,
        help="Don't print ANSI colors like ACK tool.",
    )

    parser.add_argument(
        "--statistics",
        "-t",
        dest="statistics",
        action="store_false",
        default=False,
        help="On final print excecution statistics.",
    )

    args = parser.parse_args()
    args = vars(args)

    statistics = args["statistics"]
    args["regexp"] = args["pattern"]
    args["path"] = args["directory"]

    del args["pattern"]
    del args["directory"]
    del args["statistics"]

    tool = ack(**args)

    tool.process_folders()
    tool.print_result()

    if statistics:
        duration = tool.get_duration()
        if duration is not None:
            print(f"\nComplete in {duration}ms.")


if __name__ == "__main__":
    main()
