import manager
from util.roman import getRomanNum


def translate_alien_numerals_to_arabic_numerals(input_data):
    input_data = input_data.split()

    roman_number = ''
    for word in input_data:
        # try:
        roman_number += manager.word_roman_relation_dict[word]
        # except:
        #     return None
    return getRomanNum(roman_number)
