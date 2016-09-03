import os

import parser


def generate_instance(input_data):
    result = parser.parse(input_data)
    package_name = 'parsed_data.' + result
    class_code = __import__(package_name, fromlist=True)
    obj = getattr(class_code, result)
    return obj(input_data)


def start_distribute()
