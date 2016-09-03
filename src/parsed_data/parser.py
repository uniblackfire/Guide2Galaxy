import re

from constants import WORD_ROMAN_RELATION


def parse(input_data):
    pattern_string = r'\w+\s+is\s+[IVXLCDM]'
    pattern = re.compile(pattern_string, re.IGNORECASE)
    if re.match(pattern, input_data):
        return WORD_ROMAN_RELATION
