import re
from parsed_data.question import Question
from util import translator


class how_many_question(Question):
    def get_info(self):
        pattern = re.compile(r'how\s+many\s+Credits\s+is\s+(.+)\s+(\w+)\s*\?', re.IGNORECASE)
        m = re.match(pattern, self.data)
        arabic_number = translator.translate_alien_numerals_to_arabic_numerals(m.group(1).strip())
        unit_name = m.group(2).strip()
        result = translator.calc_credits(arabic_number, unit_name)
        if result.is_integer():
            result = int(result)
        return m.group(1).strip() + ' ' + unit_name + ' is ' + str(result) + ' Credits'
