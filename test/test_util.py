import unittest
from unittest import mock

import os

import file
import util.input as input_util
from util import translator


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
        # when
        input_util.read_file = read_file_success
        # then
        self.assertIsNotNone(input_util.get_all_input_data)

    def test_translate_glob_to_1(self):
        # given
        input_data = 'glob'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 1)

    def test_translate_prok_to_5(self):
        # given
        input_data = 'prok'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 5)

    def test_translate_pish_to_10(self):
        # given
        input_data = 'pish'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 10)

    def test_translate_tegj_to_50(self):
        # given
        input_data = 'tegj'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 50)

    def test_translate_glob_glob_to_2(self):
        # given
        input_data = 'glob glob'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 2)

    def test_translate_glob_prok_to_4(self):
        # given
        input_data = 'glob prok'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 4)

    def test_translate_pish_pish_to_20(self):
        # given
        input_data = 'pish pish'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 20)

    def test_translate_pish_tegj_glob_glob_to_42(self):
        # given
        input_data = 'pish tegj glob glob'
        # when
        result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 42)
