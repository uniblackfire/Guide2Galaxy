import re

import constants
from parsed_data.question import Question
from util import translator


class how_many_question(Question):
    def get_info(self):
        pattern = re.compile(r'how\s+many\s+Credits\s+is\s+(.+)\s+(\w+)\s*\?', re.IGNORECASE)
        m = re.match(pattern, self.data)
        unit_name = m.group(2).strip()
        result = translator.calc_credits(m.group(1).strip(), unit_name)
        if result:
            if result.is_integer():
                result = int(result)
            return m.group(1).strip() + ' ' + unit_name + ' is ' + str(result) + ' Credits'
        else:
            return constants.ERROR_MSG
