import manager
from util.roman import getRomanNum


word_roman_relation_dict = dict()
money_credit_relation_dict = dict()


def translate_alien_numerals_to_arabic_numerals(input_data):
    input_data = input_data.strip().split()
    
    roman_number = ''
    for word in input_data:
        try:
            roman_number += word_roman_relation_dict[word]
        except KeyError:
            print(KeyError)
            return None
    return getRomanNum(roman_number)


def calc_credits(alien_number, unit_name):
    return translate_alien_numerals_to_arabic_numerals(alien_number) * money_credit_relation_dict[unit_name]


def get_credits_for_one_unit(unit_name):
    return money_credit_relation_dict[unit_name]
