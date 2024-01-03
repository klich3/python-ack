"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
ack.py (c) 2024 
Created:  2024-01-03 02:27:39 
Desc: ACK tool regexp search tool in folders tree
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
            num_procesos=10,
            exclude_paths_regexp=["exclude_*"],
            follow_links=False,
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
# TODO: ascii colors
# TODO: exclude text in files
# TODO : add external callback for vector search


class ack:
    start_time = None
    end_time = None
    results = {}

    def __init__(
        self,
        path,
        regexp,
        num_procesos=10,
        exclude_paths_regexp=[],
        follow_links=False,
        exclude_regexp=[],
    ):
        """
        Primary class for search
        @param path: path to search
        @param regexp: regex to search in files
        @param exclude_regexp: exclude text result in files by regexp
        @param num_procesos: number of processes
        @param exclude_paths_regexp: exclude paths by regexp
        @param follow_links: follow sys links on search
        """
        self.path = path
        self.regexp = regexp
        self.num_procesos = num_procesos
        self.exclude_regexp = exclude_regexp
        self.exclude_paths_regexp = exclude_paths_regexp
        self.follow_links = follow_links
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
            for i, line in enumerate(f, 1):
                if any(re.search(excl, line) for excl in self.exclude_regexp):
                    continue

                if re.search(self.regexp, line):
                    folder = os.path.dirname(file)
                    if folder not in results:
                        results[folder] = []
                    results[folder].append((i, line.strip()))
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
        for i in range(self.num_procesos):
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
        for i in range(self.num_procesos):
            files_queue.put(None)
        for t in threads:
            t.join()

        self.end_time = time.time()

    def print_result(self):
        """
        result print function
        """
        for folder, results in self.results.items():
            print(f"Folder: {folder}:")
            for num_linea, linea in results:
                print(f"L: {num_linea}: {linea}")

    def get_duration(self):
        """
        return execution time
        """
        if self.start_time is None or self.end_time is None:
            return None
        return (self.end_time - self.start_time) * 1000
