import re

import constants
from parsed_data.question import Question
from util import translator, regex


class how_many_credits_for_one_unit(Question):
    def get_info(self):
        groups = regex.match_to_groups(r'how\s+many\s+Credits\s+for\s+.+\s+(\w+)\s*\?',
                                       self.data, re.IGNORECASE)
        unit_name = groups[0].strip()
        result = translator.get_credits_for_one_unit(unit_name)
        if result:
            if result.is_integer():
                result = int(result)
            return unit_name + ' is ' + str(result) + ' Credits'
        else:
            return constants.ERROR_MSG
