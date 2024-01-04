# Python-ACK

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

ACK is a code-searching tool, similar to grep but optimized for programmers searching large trees of source code.

## Features
- Multi-process search
- Exclude specific paths and patterns
- ANSI color-coded output
- Search in symlinks (Python >= 2.6 only)
- Execution statistics

---

# Usage as script
***Options***
* --num-processes, -n: Number of processes to use (default: 4).
* --exclude-path, -x: Exclude paths matching EXCLUDE_PATH_PATTERN.
* --follow-links, -f: Follow symlinks (Python >= 2.6 only).
* --exclude-search, -s: Exclude results matching EXCLUDE_PATTERN.
* --no-colors, -c: Don't print ANSI colors like ACK tool.
* --statistics, -t: On final print execution statistics.


### Example

***Search:***
```shell
python -m python_ack "apple" /path/to/search
```

***Help:***
```shell
python -m python_ack --help
```

```
usage: python-ack [-h] [--num-processes NUM_PROCESSES] [--exclude-path EXCLUDE_PATH_PATTERN] [--follow-links] [--exclude-search EXCLUDE_PATTERN]
                  [--no-colors] [--statistics]
                  PATTERN [DIRECTORY]

Python-ACK is a code-searching tool, similar to grep but optimized for programmers searching large trees of source code.

positional arguments:
  PATTERN               Pattern to search for.
  DIRECTORY             A directory to search.

options:
  -h, --help            show this help message and exit
  --num-processes NUM_PROCESSES, -n NUM_PROCESSES
                        Number of processes to use.
  --exclude-path EXCLUDE_PATH_PATTERN, -x EXCLUDE_PATH_PATTERN
                        Exclude paths matching EXCLUDE_PATH_PATTERN.
  --follow-links, -f    Follow symlinks (Python >= 2.6 only).
  --exclude-search EXCLUDE_PATTERN, -s EXCLUDE_PATTERN
                        Exclude results matching EXCLUDE_PATTERN.
  --no-colors, -c       Don't print ANSI colors like ACK tool.
  --statistics, -t      On final print excecution statistics.

```

---

## Ack Class Attributes

The `ack` class in Python-ACK has several attributes that allow you to customize the behavior of the search tool. Here's a brief description of each attribute:

- **path**: The path to the directory where the search will be performed.
- **regexp**: The regular expression pattern to search for in files.
- **num_processes**: Number of processes to use for the multi-process search (default: 4).
- **exclude_paths_regexp**: A list of regular expressions to exclude paths from the search.
- **follow_links**: Boolean flag indicating whether to follow symbolic links (Python >= 2.6 only).
- **exclude_regexp**: A list of regular expressions to exclude results matching specific patterns in files.
- **use_ansi_colors**: Boolean flag indicating whether to use ANSI colors in the output.
- **search_function**: Custom search function to be used for searching in files.
- **return_as_dict**: Boolean flag indicating whether to return the result as a dictionary.


### Example Usage:

```python
from python_ack.ack import ack

def main():
    folder = "/path/to/search"
    instance = ack(
        path=folder,
        regexp="apple",
        exclude_regexp=["solor"],
        num_processes=10,
        exclude_paths_regexp=["exclude_*"],
        follow_links=False,
        use_ansi_colors=False
    )
    instance.process_folders()
    instance.print_result()

    duration = instance.get_duration()
    if duration is not None:
        print(f"\nComplete in {duration}ms.")

if __name__ == "__main__":
    main()

```

---

### Local dev

In root folder run `pip install -e .`

```shell
cd /tests
python test.py
```

## Local cli run

```shell
python -m python_ack
```

---

# Acknowledgements
* Author: Anton Sychev
* Email: anton@sychev.xyz


# License
This project is licensed under the MIT License - see the LICENSE file for details.


Make sure to replace "/path/to/search" with your actual path. You can also customize the badges, add more sections, and provide more details based on your project's needs.


---

### Publish to Pypi

***Local:***
```shell
python -m pip install build twine
python3 -m build   
twine check dist/*
twine upload dist/*
```

***Live:***
No need do nothing GitHub have Workflow action its publish auto