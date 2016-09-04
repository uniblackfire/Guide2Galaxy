import re

from util import regex
from parsed_data.intergalactic_earth_relation import IntergalacticEarthRelation


class word_roman_relation(IntergalacticEarthRelation):
    def __init__(self, data):
        groups = regex.match_to_groups(r'(\w+)\s+is\s+([IVXLCDM])',
                                       data, re.IGNORECASE)
        self.word = groups[0]
        self.roman = groups[1]

    def get_info(self):
        return self.word, self.roman
