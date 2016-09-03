from parsed_data.parsed_abstract import Parsed


class error(Parsed):
    def __init__(self, data):
        self.data = data

    def get_info(self):
        return 'I have no idea what you are talking about'
