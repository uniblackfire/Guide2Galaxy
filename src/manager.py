import os

import file
import parser
import util.input as input_util
from parsed_data.money_credit_relation import money_credit_relation
from parsed_data.question import Question
from parsed_data.error import error

from parsed_data.word_roman_relation import word_roman_relation
from util import my_console

word_roman_relation_dict = dict()
money_credit_relation_list = list()


def generate_instance(input_data):
    result = parser.parse(input_data)
    if result:
        package_name = 'parsed_data.' + result
        class_code = __import__(package_name, fromlist=True)
        obj = getattr(class_code, result)
        return obj(input_data)
    else:
        return None


def process_parsed_data_instance(instance):
    if isinstance(instance, word_roman_relation):
        global word_roman_relation_dict
        word_roman_relation_dict[instance.get_info()[0]] = instance.get_info()[1]

    if isinstance(instance, money_credit_relation):
        global money_credit_relation_list
        money_credit_relation_list.append(instance)

    if isinstance(instance, Question) or isinstance(instance, error):
        my_console.output(instance.get_info())


def start_process():
    filename = os.path.join(file.project_dir, 'data/input.txt')
    input_data = input_util.get_all_input_data(filename)
    data_list = input_data.split('\n')

    for data_item in data_list:
        instance = generate_instance(data_item)
        if not instance:
            continue
        process_parsed_data_instance(instance)
