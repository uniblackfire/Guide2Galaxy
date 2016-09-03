import re


from parsed_data.intergalactic_earth_relation import IntergalacticEarthRelation


class word_roman_relation(IntergalacticEarthRelation):
    def __init__(self, data):
        data_split = data.split('is')
        self.word = data_split[0].strip()
        self.roman = data_split[1].strip()

    def get_info(self):
        return self.word, self.roman
