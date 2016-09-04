import unittest
from unittest import mock
from unittest.mock import patch
import os

import file
import manager
import util.input as input_util
from parsed_data.word_roman_relation import word_roman_relation
from util import translator


class TestUtil(unittest.TestCase):
    def setUp(self):
        word_roman_relation_a = word_roman_relation('glob is I')
        word_roman_relation_b = word_roman_relation('prok is V')
        word_roman_relation_c = word_roman_relation('pish is X')
        word_roman_relation_d = word_roman_relation('tegj is L')
        word_roman_relation_list = [word_roman_relation_a,
                                    word_roman_relation_b,
                                    word_roman_relation_c,
                                    word_roman_relation_d]
        self.word_roman_relation_dict = dict()
        for item in word_roman_relation_list:
            self.word_roman_relation_dict[item.get_info()[0]] = item.get_info()[1]

    def tearDown(self):
        pass

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
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 1)

    def test_translate_prok_to_5(self):
        # given
        input_data = 'prok'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 5)

    def test_translate_pish_to_10(self):
        # given
        input_data = 'pish'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 10)

    def test_translate_tegj_to_50(self):
        # given
        input_data = 'tegj'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 50)

    def test_translate_glob_glob_to_2(self):
        # given
        input_data = 'glob glob'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 2)

    def test_translate_glob_prok_to_4(self):
        # given
        input_data = 'glob prok'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 4)

    def test_translate_pish_pish_to_20(self):
        # given
        input_data = 'pish pish'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 20)

    def test_translate_pish_tegj_glob_glob_to_42(self):
        # given
        input_data = 'pish tegj glob glob'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)        # then
        self.assertEqual(result, 42)
