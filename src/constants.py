WORD_ROMAN_RELATION = 'word_roman_relation'
MONEY_CREDIT_RELATION = 'money_credit_relation'
HOW_MUCH_QUESTION = 'how_much_question'
HOW_MANY_QUESTION = 'how_many_question'

PATTERN_STRINGS = [
    (r'\w+\s+is\s+[IVXLCDM]', WORD_ROMAN_RELATION),
    (r'.+\s+is\s+\d+\s+Credits', MONEY_CREDIT_RELATION),
    (r'how\s+much\s+is\s+.+\?', HOW_MUCH_QUESTION),
    (r'how\s+many\s+Credits\s+is\s+.+\?', HOW_MANY_QUESTION)
]
