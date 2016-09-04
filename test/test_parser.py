import unittest
from unittest import mock
from unittest.mock import patch

import manager
import parser
from constants import WORD_ROMAN_RELATION, MONEY_CREDIT_RELATION, HOW_MUCH_QUESTION, HOW_MANY_QUESTION
from parsed_data.money_credit_relation import money_credit_relation
from parsed_data.word_roman_relation import word_roman_relation


class TestParser(unittest.TestCase):
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

    def test_word_roman_relation_init_field(self):
        # given
        input_data = 'tegj is L'
        # when
        obj = word_roman_relation(input_data)
        # then
        self.assertEqual(obj.word, 'tegj')
        self.assertEqual(obj.roman, 'L')

    def test_parse_word_roman_relation(self):
        # given
        input_data = 'tegj is L'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, WORD_ROMAN_RELATION)

    def test_money_credit_relation_init_field(self):
        # given
        input_data = 'glob glob Silver is 34 Credits'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            obj = money_credit_relation(input_data)
        # then
        self.assertEqual(obj.number, 2)
        self.assertEqual(obj.unit, 'Silver')
        self.assertEqual(obj.value, 34)

    def test_parse_money_credit_relation(self):
        # given
        input_data = 'glob glob Silver is 34 Credits'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, MONEY_CREDIT_RELATION)

    def test_parse_how_much_question(self):
        # given
        input_data = 'how much is pish tegj glob glob ?'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, HOW_MUCH_QUESTION)

    def test_parse_how_many_question(self):
        # given
        input_data = 'how many Credits is glob prok Silver ?'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, HOW_MANY_QUESTION)
