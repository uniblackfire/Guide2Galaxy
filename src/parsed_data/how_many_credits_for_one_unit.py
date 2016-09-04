import re

import constants
from parsed_data.question import Question
from util import translator


class how_many_credits_for_one_unit(Question):
    def get_info(self):
        pattern = re.compile(r'how\s+many\s+Credits\s+for\s+.+\s+(\w+)\s*\?', re.IGNORECASE)
        m = re.match(pattern, self.data)
        unit_name = m.group(1).strip()
        result = translator.get_credits_for_one_unit(unit_name)
        if result:
            if result.is_integer():
                result = int(result)
            return unit_name + ' is ' + str(result) + ' Credits'
        else:
            return constants.ERROR_MSG
