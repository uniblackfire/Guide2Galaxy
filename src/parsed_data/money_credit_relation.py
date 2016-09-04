import re
from parsed_data.intergalactic_earth_relation import IntergalacticEarthRelation
from util import translator, regex


class money_credit_relation(IntergalacticEarthRelation):
    def __init__(self, data):
        groups = regex.match_to_groups(r'(.+)\s+(\w+)\s+is\s+(\d+)\s+Credits',
                                       data, re.IGNORECASE)
        self.number = translator.translate_alien_numerals_to_arabic_numerals(groups[0].strip())
        self.unit = groups[1]
        self.value = int(groups[2])

    def get_info(self):
        return self.unit, self.value / self.number
