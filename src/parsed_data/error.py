import constants
from parsed_data.parsed_abstract import Parsed


class error(Parsed):
    def __init__(self, data):
        self.data = data

    def get_info(self):
        return constants.ERROR_MSG
