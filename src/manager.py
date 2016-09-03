import os

import parser


def read_file(filename):
    if not os.path.isfile(filename):
        return None

    file_content = ''
    with open(filename, 'r') as fd:
        for line in fd:
            file_content += line

    return file_content


def generate_instance(input_data):
    result = parser.parse(input_data)
    package_name = 'parsed_data.' + result
    class_code = __import__(package_name, fromlist=True)
    obj = getattr(class_code, result)
    return obj(input_data)
