import re

from constants import *


def get_re_pattern(pattern_string):
    return re.compile(pattern_string, re.IGNORECASE)


def parse(input_data):
    for ps in PATTERN_STRINGS:
        pattern = get_re_pattern(ps[0])
        if re.match(pattern, input_data):
            return ps[1]
    return ERROR


def generate_instance(input_data):
    result = parse(input_data)
    if result:
        package_name = 'parsed_data.' + result
        class_code = __import__(package_name, fromlist=True)
        obj = getattr(class_code, result)
        return obj(input_data)
    else:
        return None
