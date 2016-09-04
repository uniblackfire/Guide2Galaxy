import os

import file
import parser
from parsed_data.question import Question
from parsed_data.error import error
from parsed_data.money_credit_relation import money_credit_relation
from parsed_data.word_roman_relation import word_roman_relation

import util.input as input_util
from util import output
from util import translator


def process_parsed_data_instance(instance):
    if isinstance(instance, word_roman_relation):
        translator.word_roman_relation_dict[instance.get_info()[0]] = instance.get_info()[1]

    if isinstance(instance, money_credit_relation):
        translator.money_credit_relation_dict[instance.get_info()[0]] = instance.get_info()[1]

    if isinstance(instance, Question) or isinstance(instance, error):
        output.output(instance.get_info())


def start_process():
    filename = os.path.join(file.project_dir, 'data/input.txt')
    input_data = input_util.get_all_input_data(filename)
    data_list = input_data.split('\n')

    for data_item in data_list:
        instance = parser.generate_instance(data_item)
        if not instance:
            continue
        process_parsed_data_instance(instance)
