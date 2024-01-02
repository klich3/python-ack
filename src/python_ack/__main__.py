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

#TODO: complete options
#TODO: search worker and init

def main():
    parser = argparse.ArgumentParser(description="ACK search tool")
    
    parser.add_argument(
        "pattern",
        metavar="PATTERN",
        action="store",
        help="a python re regular expression",
    )

    if sys.version_info >= (2, 6):
        parser.add_argument(
            "--follow-links",
            "-s",
            dest="follow_links",
            action="store_true",
            default=False,
            help="follow symlinks (Python >= 2.6 only)",
        )

    parser.add_argument(
        "--binary",
        "-b",
        dest="search_binary",
        action="store_true",
        default=False,
        help="search binary files",
    )
    parser.add_argument(
        "--no-colors",
        "-c",
        dest="use_ansi_colors",
        action="store_false",
        default=True,
        help="don't print ANSI colors",
    )

    parser.add_argument(
        "--exclude",
        "-x",
        metavar="PATH_PATTERN",
        dest="exclude_path_patterns",
        action="append",
        default=[],
        type=str,
        help="exclude paths matching PATH_PATTERN",
    )

    parser.add_argument(
        "directory",
        metavar="DIRECTORY",
        nargs="?",
        default=os.getcwd(),
        help="a directory to search in (default cwd)",
    )

    flags = 0
    args = parser.parse_args()
    pattern = re.escape(args.pattern) if args.escape else args.pattern

    tool = ack(
            regex=re.compile(pattern, flags),
            number_processes=args.number_processes,
        )
    
    print("\n--", tool)

if __name__ == "__main__":
    main()