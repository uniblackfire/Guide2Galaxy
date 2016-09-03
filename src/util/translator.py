from util.roman import getRomanNum


def translate_alien_numerals_to_arabic_numerals(input_data, word_roman_relation_list):
    input_data = input_data.split()

    word_roman_dict = dict()
    for item in word_roman_relation_list:
        word_roman_dict[item.get_info()[0]] = item.get_info()[1]

    roman_number = ''
    for word in input_data:
        roman_number += word_roman_dict[word]

    return getRomanNum(roman_number)
