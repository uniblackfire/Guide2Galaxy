import unittest

from parsed_data import parser


class TestParser(unittest.TestCase):
    def test_parse_method(self):
        # given
        input_data = 'tegj is L'
        # when
        result = parser.parse()
        # then
        self.assertIsNotNone(result)
