"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
ack.py (c) 2024 
Created:  2024-01-03 02:27:39 
Desc: ACK tool regexp search tool in folders tree
Docs: 
    * ascii color scheme:
        \033[30m: Black
        \033[32m: Green
        \033[33m: Yellow
        \033[43m: Yellow background
        \033[0m: Reset color
Sample:
    import os
    import sys

    from python_ack.ack import ack


    def main():
        folder = os.path.join(os.getcwd(), "tests", "crw")

        instance = ack(
            path=folder,
            regexp="apple",
            exclude_regexp=["solor"],
            num_processes=10,
            exclude_paths_regexp=["exclude_*"],
            follow_links=False,
            use_ansi_colors=False
            return_as_dict=True
        )
        instance.process_folders()
        instance.print_result()

        duration = instance.get_duration()
        if duration is not None:
            print(f"\nComplete in {duration}ms.")


    if __name__ == "__main__":
        main()
"""

import os, re, multiprocessing, time
import concurrent.futures
from queue import Queue
from threading import Thread

# TODO: return print / return array
# TODO : add external callback for vector search


class ack:
    start_time = None
    end_time = None
    results = {}

    def __init__(
        self,
        path,
        regexp,
        num_processes=10,
        exclude_paths_regexp=[],
        follow_links=False,
        exclude_regexp=[],
        use_ansi_colors=True,
        search_function=None,
        return_as_dict=False,
    ):
        """
        Primary class for search
        @param path: path to search
        @param regexp: regex to search in files
        @param exclude_regexp: exclude text result in files by regexp
        @param num_processes: number of processes
        @param exclude_paths_regexp: exclude paths by regexp
        @param follow_links: follow sys links on search

        @param use_ansi_colors: use ansi colors in output

        @param search_function: function to search in files
        @param return_as_dict: return result as dict
        """
        self.path = path
        self.regexp = regexp
        self.num_processes = num_processes
        self.exclude_regexp = exclude_regexp
        self.exclude_paths_regexp = exclude_paths_regexp
        self.follow_links = follow_links
        self.use_ansi_colors = use_ansi_colors
        self.search_function = search_function
        self.return_as_dict = return_as_dict
        self.files = Queue()

    @staticmethod
    def is_excluded(name, regexps):
        return any(re.search(regexp, name) for regexp in regexps)

    def search(self, file):
        """
        Search in files
        @param file: file to search
        """
        results = {}

        with open(file, "r", errors="ignore") as f:
            # custom search function
            # TODO: test
            if self.search_function is not None:
                return self.search_function(f)

            for i, line in enumerate(f, 1):
                if any(re.search(excl, line) for excl in self.exclude_regexp):
                    continue

                match = re.search(self.regexp, line)
                if match:
                    folder = os.path.dirname(file)
                    if folder not in results:
                        results[folder] = []
                    highlighted = (
                        line[: match.start()]
                        + (
                            ("\033[43m\033[30m" if self.use_ansi_colors else "")
                            + line[match.start() : match.end()]
                            + ("\033[0m" if self.use_ansi_colors else "")
                        )
                        + line[match.end() :]
                    )
                    results[folder].append((i, highlighted.strip()))
        return results

    def process_folders(self):
        """
        worker function
        """
        self.start_time = time.time()
        files_queue = Queue()

        def worker():
            while True:
                file = files_queue.get()
                if file is None:
                    break
                results = self.search(file)
                for folder, res in results.items():
                    if folder not in self.results:
                        self.results[folder] = []
                    self.results[folder].extend(res)
                files_queue.task_done()

        threads = []
        for i in range(self.num_processes):
            t = Thread(target=worker)
            t.start()
            threads.append(t)

        for root, dirs, file_list in os.walk(self.path, followlinks=self.follow_links):
            dirs[:] = [
                d for d in dirs if not self.is_excluded(d, self.exclude_paths_regexp)
            ]

            # add files to queue
            for file in file_list:
                full_file_path = os.path.join(root, file)
                if not self.is_excluded(full_file_path, self.exclude_paths_regexp):
                    files_queue.put(full_file_path)

        # block until all tasks are done
        files_queue.join()

        # stop workers
        for i in range(self.num_processes):
            files_queue.put(None)
        for t in threads:
            t.join()

        self.end_time = time.time()

    def print_result(self):
        """
        result print function
        Sample:
            instance = ack(
                return_as_dict=True
            )
            result = instance.print_result()
            print(result)
            {'/Users/too-off/www_211/python-ack/tests/crw/memories/glOtc6EzYQTZEt0J18cU1f4Ycdz1H8WWTDVkBQTp1Gv2BWgb': {2: '"content": "One fruit: \x1b[43m\x1b[30mapple\x1b[0m",', 20: '"\x1b[43m\x1b[30mapple\x1b[0m alguna frase mas",', 27: '"\x1b[43m\x1b[30mapple\x1b[0m solor",'}, '/Users/too-off/www_211/python-ack/tests/crw/memories/exclude_dir': {2: '"content": "One fruit: \x1b[43m\x1b[30mapple\x1b[0m",'}}
        """
        if self.return_as_dict:
            result_dict = {}
            for folder, matches in self.results.items():
                result_dict[folder] = {}
                for match in matches:
                    result_dict[folder][match[0]] = match[1]
            return result_dict
        else:
            for folder, matches in self.results.items():
                print(
                    ("\033[32m" if self.use_ansi_colors else "")
                    + folder
                    + ("\033[0m" if self.use_ansi_colors else "")
                )  # Print folder in green
                for line_number, line in matches:
                    print(
                        ("\033[33m" if self.use_ansi_colors else "")
                        + str(line_number)
                        + ("\033[0m: " if self.use_ansi_colors else ": ")
                        + line
                    )  # Print line number in yellow

    def get_duration(self):
        """
        return execution time
        """
        if self.start_time is None or self.end_time is None:
            return None
        return (self.end_time - self.start_time) * 1000
