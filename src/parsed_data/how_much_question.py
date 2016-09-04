import re
from parsed_data.question import Question
from util import translator


class how_much_question(Question):
    def get_info(self):
        pattern = re.compile(r'how\s+much\s+is\s+(.+?)\s*\?', re.IGNORECASE)

        alien_number = re.match(pattern, self.data).group(1)
        arabic_number = translator.translate_alien_numerals_to_arabic_numerals(alien_number)
        return alien_number + ' is ' + str(arabic_number)
