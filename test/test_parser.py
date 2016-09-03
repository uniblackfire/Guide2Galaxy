import unittest

from constants import WORD_ROMAN_RELATION
from parsed_data import parser


class TestParser(unittest.TestCase):
    def test_parse_word_roman_relation(self):
        # given
        input_data = 'tegj is L'
        # when
        result = parser.parse(input_data)
        # then
        self.assertIs(result, WORD_ROMAN_RELATION)
