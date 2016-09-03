import unittest
from unittest import mock
import os

import file
import src.manager as manager
from parsed_data.how_many_question import how_many_question
from parsed_data.how_much_question import how_much_question
from parsed_data.money_credit_relation import money_credit_relation
from parsed_data.word_roman_relation import word_roman_relation


class TestManager(unittest.TestCase):
    def test_read_file_method(self):
        # given
        filename = os.path.join(file.project_dir, 'data/input.txt')
        # when
        content = manager.read_file(filename)
        # then
        self.assertIsNotNone(content)

    def test_generate_word_roman_number_relation_instance_accord_to_input(self):
        # given
        input_line = 'glob is I'
        # when
        instance = manager.generate_instance(input_line)
        # then
        self.assertIsInstance(instance, word_roman_relation)

    def test_generate_money_credit_relation_instance_accord_to_input(self):
        # given
        input_line = 'glob glob Silver is 34 Credits'
        # when
        instance = manager.generate_instance(input_line)
        # then
        self.assertIsInstance(instance, money_credit_relation)

    def test_generate_how_much_question_instance_accord_to_input(self):
        # given
        input_line = 'how much is pish tegj glob glob ?'
        # when
        instance = manager.generate_instance(input_line)
        # then
        self.assertIsInstance(instance, how_much_question)

    def test_generate_how_many_question_instance_accord_to_input(self):
        # given
        input_line = 'how many Credits is glob prok Silver ?'
        # when
        instance = manager.generate_instance(input_line)
        # then
        self.assertIsInstance(instance, how_many_question)
