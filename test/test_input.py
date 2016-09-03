import unittest
from unittest import mock

import src.manager as manager

class TestInput(unittest.TestCase):
    def test_read_file(self):
        # given
        filename = '/Users/jiayizhang/code/PycharmProjects/Guide2Galaxy/data/input.txt'
        # when
        content = manager.read_file(filename)
        # then
        assert content is not None
