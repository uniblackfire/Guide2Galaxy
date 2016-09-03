import unittest
from unittest import mock

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

    def test_get_all_input_data(self):
        # given
        read_file_success = mock.Mock(return_value='file content')
        #when
        input_util.read_file = read_file_success
        #then
        self.assertIsNotNone(input_util.get_all_input_data)
