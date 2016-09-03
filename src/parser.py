import re

from constants import *

PATTERN_STRINGS = [
    (r'\w+\s+is\s+[IVXLCDM]', WORD_ROMAN_RELATION),
    (r'.+\s+is\s+\d+\s+Credits', MONEY_CREDIT_RELATION),
    (r'how\s+much\s+is\s+.+\?', HOW_MUCH_QUESTION),
    (r'how\s+many\s+Credits\s+is\s+.+\?', HOW_MANY_QUESTION)
]


def get_re_pattern(pattern_string):
    return re.compile(pattern_string, re.IGNORECASE)


def parse(input_data):
    for ps in PATTERN_STRINGS:
        pattern = get_re_pattern(ps[0])
        if re.match(pattern, input_data):
            return ps[1]
    return None
