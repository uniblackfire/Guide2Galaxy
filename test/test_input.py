import unittest
from unittest import mock
import os

import file
import src.manager as manager

class TestInput(unittest.TestCase):
    def test_read_file(self):
        # given
        filename = os.path.join(file.project_dir, 'data/input.txt')
        # when
        content = manager.read_file(filename)
        # then
        assert content is not None
