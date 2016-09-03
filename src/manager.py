import os

import file
import parser
import util.input as input_util


def generate_instance(input_data):
    result = parser.parse(input_data)
    if result:
        package_name = 'parsed_data.' + result
        class_code = __import__(package_name, fromlist=True)
        obj = getattr(class_code, result)
        return obj(input_data)
    else:
        return None


def start_process():
    filename = os.path.join(file.project_dir, 'data/input.txt')
    input_data = input_util.get_all_input_data(filename)
    data_list = input_data.split('\n')
    for data_item in data_list:
        instance = generate_instance(data_item)

