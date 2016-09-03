import unittest

import parser
from constants import WORD_ROMAN_RELATION, MONEY_CREDIT_RELATION, HOW_MUCH_QUESTION, HOW_MANY_QUESTION


class TestParser(unittest.TestCase):
    def test_parse_word_roman_relation(self):
        # given
        input_data = 'tegj is L'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, WORD_ROMAN_RELATION)

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
