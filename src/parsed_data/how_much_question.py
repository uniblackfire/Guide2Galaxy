import re

import constants
from parsed_data.question import Question
from util import translator, regex


class how_much_question(Question):
    def get_info(self):
        groups = regex.match_to_groups(r'how\s+much\s+is\s+(.+?)\s*\?',
                                       self.data, re.IGNORECASE)
        alien_number = groups[0].strip()
        arabic_number = translator.translate_alien_numerals_to_arabic_numerals(alien_number)
        if arabic_number:
            return alien_number + ' is ' + str(arabic_number)
        else:
            return constants.ERROR_MSG
