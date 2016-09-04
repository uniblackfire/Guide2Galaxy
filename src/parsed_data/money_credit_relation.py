import re
from parsed_data.intergalactic_earth_relation import IntergalacticEarthRelation
from util import translator


class money_credit_relation(IntergalacticEarthRelation):
    def __init__(self, data):
        pattern = re.compile(r'(.+)\s+(\w+)\s+is\s+(\d+)\s+Credits', re.IGNORECASE)
        m = re.match(pattern, data)

        self.number = translator.translate_alien_numerals_to_arabic_numerals(m.group(1))
        self.unit = m.group(2)
        self.value = int(m.group(3))

    def get_info(self):
        pass
