import re

import constants
from parsed_data.question import Question
from util import translator, regex


class how_many_question(Question):
    def get_info(self):
        groups = regex.match_to_groups(r'how\s+many\s+Credits\s+is\s+(.+)\s+(\w+)\s*\?',
                                       self.data, re.IGNORECASE)
        alien_number = groups[0].strip()
        unit_name = groups[1].strip()
        result = translator.calc_credits(alien_number, unit_name)
        if result:
            if result.is_integer():
                result = int(result)
            return alien_number + ' ' + unit_name + ' is ' + str(result) + ' Credits'
        else:
            return constants.ERROR_MSG
