import unittest
from unittest import mock
import os

import file
import src.manager as manager


class TestInput(unittest.TestCase):
    def test_read_file_method(self):
        # given
        filename = os.path.join(file.project_dir, 'data/input.txt')
        # when
        content = manager.read_file(filename)
        # then
        self.assertIsNotNone(content)

    def test_generate_word_roman_number_relation_instance_accord_to_input(self):
        # given
        input_line = 'glob is I'
        # when
        instance = manager.generate_instance(input_line)
        # then
        self.assertIsNotNone(instance)
