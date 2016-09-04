import manager
from util.roman import getRomanNum


def translate_alien_numerals_to_arabic_numerals(input_data):
    input_data = input_data.strip().split()
    
    roman_number = ''
    for word in input_data:
        try:
            roman_number += manager.word_roman_relation_dict[word]
        except KeyError:
            print(KeyError)
            return None
    return getRomanNum(roman_number)


def calc_credits(arabic_number, unit_name):
    return arabic_number * manager.money_credit_relation_dict[unit_name]
