from parsed_data.parsed_abstract import Parsed


class IntergalacticEarthRelation(Parsed):
    def __init__(self, data):
        data_split = data.split('is')
        self.what = data_split[0]
        self.sth = data_split[1]
