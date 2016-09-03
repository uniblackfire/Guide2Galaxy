import unittest

import os

import file
import util.input as input_util


class TestUtil(unittest.TestCase):
    def test_read_file_method(self):
        # given
        filename = os.path.join(file.project_dir, 'data/input.txt')
        # when
        content = input_util.read_file(filename)
        # then
        self.assertIsNotNone(content)
