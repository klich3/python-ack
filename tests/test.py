"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz) 
test.py (c) 2024 
Created:  2024-01-04 00:14:32 
Desc: test cases
"""

# TODO: complete test unit

"""
import unittest
from python_ack.ack import ack


class TestAck(unittest.TestCase):
    def setUp(self):
        self.ack_instance = ack(
            path=".",
            regexp="apple",
            num_processes=4,
            exclude_paths_regexp=[],
            follow_links=False,
            exclude_regexp=["2"],
            use_ansi_colors=True,
            return_as_dict=False,
        )

    def test_is_excluded(self):
        self.assertFalse(self.ack_instance.is_excluded("filename.txt", ["apple"]))
        # Test when filename matches the regexp
        self.assertTrue(self.ack_instance.is_excluded("apple_filename.txt", ["apple"]))


if __name__ == "__main__":
    unittest.main()

"""
