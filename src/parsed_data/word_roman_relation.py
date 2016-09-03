import re


from parsed_data.intergalactic_earth_relation import IntergalacticEarthRelation


class word_roman_relation(IntergalacticEarthRelation):
    def __init__(self, data):
        pattern = re.compile(r'(\w+)\s+is\s+([IVXLCDM])')
        m = re.match(pattern, data)
        self.word = m.group(1)
        self.roman = m.group(2)

    def get_info(self):
        return self.word, self.roman
