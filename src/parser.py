import re

from constants import *


def get_re_pattern(pattern_string):
    return re.compile(pattern_string, re.IGNORECASE)


def parse(input_data):
    for ps in PATTERN_STRINGS:
        pattern = get_re_pattern(ps[0])
        if re.match(pattern, input_data):
            return ps[1]
    return None
