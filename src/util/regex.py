import re


def match_to_groups(pattern_string, string, flag=0):
    m = re.match(pattern_string, string, flag)
    return m.groups()
