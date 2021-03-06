import unittest
from unittest import mock
from unittest.mock import patch
import os
import re

import file
import manager
import util.input as input_util
from parsed_data.money_credit_relation import money_credit_relation
from parsed_data.word_roman_relation import word_roman_relation
from util import translator, output, regex
from util.roman import getRomanNum


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

        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            self.silver_credit_relation = money_credit_relation('glob glob Silver is 34 Credits')
            self.gold_credit_relation = money_credit_relation('glob prok Gold is 57800 Credits')
            self.iron_credit_relation = money_credit_relation('pish pish Iron is 3910 Credits')
        money_credit_relation_list = [self.silver_credit_relation,
                                      self.gold_credit_relation,
                                      self.iron_credit_relation]
        self.money_credit_relation_dict = dict()
        for item in money_credit_relation_list:
            self.money_credit_relation_dict[item.get_info()[0]] = item.get_info()[1]

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
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)
        # then
        self.assertEqual(result, 1)

    def test_translate_prok_to_5(self):
        # given
        input_data = 'prok'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 5)

    def test_translate_pish_to_10(self):
        # given
        input_data = 'pish'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 10)

    def test_translate_tegj_to_50(self):
        # given
        input_data = 'tegj'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 50)

    def test_translate_glob_glob_to_2(self):
        # given
        input_data = 'glob glob'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 2)

    def test_translate_glob_prok_to_4(self):
        # given
        input_data = 'glob prok'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 4)

    def test_translate_pish_pish_to_20(self):
        # given
        input_data = 'pish pish'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 20)

    def test_translate_pish_tegj_glob_glob_to_42(self):
        # given
        input_data = 'pish tegj glob glob'
        # when
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            result = translator.translate_alien_numerals_to_arabic_numerals(input_data)

        # then
        self.assertEqual(result, 42)

    def test_getRomanNum(self):
        roman_arabic_dict = {'I': 1,
                             'II': 2,
                             'III': 3,
                             'IV': 4,
                             'V': 5,
                             'VI': 6,
                             'VII': 7,
                             'VIII': 8,
                             'IX': 9,
                             'X': 10,
                             'XI': 11,
                             'XII': 12,
                             'XIII': 13,
                             'XIV': 14,
                             'XV': 15,
                             'XVI': 16,
                             'XVII': 17,
                             'XVIII': 18,
                             'XIX': 19,
                             'XX': 20,
                             'XXX': 30,
                             'XL': 40,
                             'L': 50,
                             'LX': 60,
                             'LXX': 70,
                             'LXXX': 80,
                             'XC': 90,
                             'XCIX': 99,
                             'C': 100,
                             'CI': 101,
                             'CII': 102,
                             'CXCIX': 199,
                             'CC': 200,
                             'CCC': 300,
                             'CD': 400,
                             'D': 500,
                             'DC': 600,
                             'DCCC': 800,
                             'CM': 900,
                             'M': 1000,
                             'MCD': 1400,
                             'MCDXXXVII': 1437,
                             'MD': 1500,
                             'MDCCC': 1800,
                             'MDCCCLXXX': 1880,
                             'MCM': 1900,
                             'MM': 2000,
                             'MMM': 3000,
                             'MMMCCCXXXIII': 3333,
                             }
        for k, v in roman_arabic_dict.items():
            self.assertEqual(getRomanNum(k), v)

    def test_console_output(self):
        output_data = 'this is what i want to say.'
        result = output.output(output_data)
        self.assertTrue(result)

    def test_calc_credits(self):
        with patch.dict(translator.word_roman_relation_dict, self.word_roman_relation_dict):
            with patch.dict(translator.money_credit_relation_dict, self.money_credit_relation_dict):
                result = translator.calc_credits('glob prok', 'Silver')
        self.assertEqual(result, 68)

    def test_get_credits_for_one_unit(self):
        with patch.dict(translator.money_credit_relation_dict, self.money_credit_relation_dict):
            result = translator.get_credits_for_one_unit('Silver')
        self.assertEqual(result, 17)

    def test_re_match_to_groups(self):
        result = regex.match_to_groups(r"how\s+much\s+is\s+(.+?)\s*\?", "how much is pish tegj glob glob ?")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 'pish tegj glob glob')
