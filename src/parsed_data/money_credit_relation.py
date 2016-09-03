from parsed_data.intergalactic_earth_relation import IntergalacticEarthRelation


class money_credit_relation(IntergalacticEarthRelation):
    def __init__(self, data, word_roman_relation_list):
        data_split = data.split('is')
        self.what = data_split[0].strip()
        self.sth = data_split[1].strip()
        self.word_roman_relation_list = word_roman_relation_list

    def get_info(self):
        pass
