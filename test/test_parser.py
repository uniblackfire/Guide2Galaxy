import unittest
from unittest import mock
from unittest.mock import patch

import manager
import parser
from constants import WORD_ROMAN_RELATION, MONEY_CREDIT_RELATION, HOW_MUCH_QUESTION, HOW_MANY_QUESTION
from parsed_data.how_many_question import how_many_question
from parsed_data.how_much_question import how_much_question
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

        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            self.silver_credit_relation = money_credit_relation('glob glob Silver is 34 Credits')
            self.gold_credit_relation = money_credit_relation('glob prok Gold is 57800 Credits')
            self.iron_credit_relation = money_credit_relation('pish pish Iron is 3910 Credits')
        money_credit_relation_list = [self.silver_credit_relation,
                                      self.gold_credit_relation,
                                      self.iron_credit_relation]
        self.money_credit_relation_dict = dict()
        for item in money_credit_relation_list:
            self.money_credit_relation_dict[item.get_info()[0]] = item.get_info()[1]

    def test_word_roman_relation_init_field(self):
        # given
        input_data = 'tegj is L'
        # when
        obj = word_roman_relation(input_data)
        # then
        self.assertEqual(obj.word, 'tegj')
        self.assertEqual(obj.roman, 'L')

    def test_word_roman_relation_get_info(self):
        # given
        input_data = 'tegj is L'
        # when
        obj = word_roman_relation(input_data)
        # then
        self.assertEqual(obj.get_info()[0], 'tegj')
        self.assertEqual(obj.get_info()[1], 'L')

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

    def test_money_credit_relation_get_info_Silver(self):
        self.assertEqual(self.silver_credit_relation.get_info()[0], 'Silver')
        self.assertEqual(self.silver_credit_relation.get_info()[1], 34 / 2)

    def test_money_credit_relation_get_info_Gold(self):

        self.assertEqual(self.gold_credit_relation.get_info()[0], 'Gold')
        self.assertEqual(self.gold_credit_relation.get_info()[1], 57800 / 4)

    def test_money_credit_relation_get_info_Iron(self):
        self.assertEqual(self.iron_credit_relation.get_info()[0], 'Iron')
        self.assertEqual(self.iron_credit_relation.get_info()[1], 3910 / 20)

    def test_parse_money_credit_relation(self):
        # given
        input_data = 'glob glob Silver is 34 Credits'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, MONEY_CREDIT_RELATION)

    def test_how_much_question_get_info(self):
        # given
        input_data = 'how much is pish tegj glob glob ?'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            result = how_much_question(input_data).get_info()
        # then
        self.assertEqual(result, 'pish tegj glob glob is 42')

    def test_parse_how_much_question(self):
        # given
        input_data = 'how much is pish tegj glob glob ?'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, HOW_MUCH_QUESTION)

    def test_how_many_question_get_info(self):
        # given
        input_data = 'how many Credits is glob prok Silver ?'
        # when
        with patch.dict(manager.word_roman_relation_dict, self.word_roman_relation_dict):
            with patch.dict(manager.money_credit_relation_dict, self.money_credit_relation_dict):
                result = how_many_question(input_data).get_info()
        # then
        self.assertEqual(result, 'glob prok Silver is 68 Credits')

    def test_parse_how_many_question(self):
        # given
        input_data = 'how many Credits is glob prok Silver ?'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, HOW_MANY_QUESTION)
