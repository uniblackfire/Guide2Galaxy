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
            return None
    return getRomanNum(roman_number)


def calc_credits(alien_number, unit_name):
    arabic_number = translate_alien_numerals_to_arabic_numerals(alien_number)
    if arabic_number and unit_name in money_credit_relation_dict:
        return arabic_number * money_credit_relation_dict[unit_name]
    else:
        return None


def get_credits_for_one_unit(unit_name):
    if unit_name in money_credit_relation_dict:
        return money_credit_relation_dict[unit_name]
    else:
        return None
