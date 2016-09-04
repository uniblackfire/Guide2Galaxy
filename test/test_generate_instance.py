import unittest
from unittest import mock
import os

import file
import manager
from parsed_data.how_many_question import how_many_question
from parsed_data.how_much_question import how_much_question
from parsed_data.money_credit_relation import money_credit_relation
from parsed_data.word_roman_relation import word_roman_relation
from parsed_data.error import error
from parser import generate_instance


class TestManager(unittest.TestCase):
    def test_generate_word_roman_number_relation_instance_accord_to_input(self):
        # given
        input_line = 'glob is I'
        # when
        instance = generate_instance(input_line)
        # then
        self.assertIsInstance(instance, word_roman_relation)

    def test_generate_money_credit_relation_instance_accord_to_input(self):
        # given
        input_line = 'glob glob Silver is 34 Credits'
        # when
        instance = generate_instance(input_line)
        # then
        self.assertIsInstance(instance, money_credit_relation)

    def test_generate_how_much_question_instance_accord_to_input(self):
        # given
        input_line = 'how much is pish tegj glob glob ?'
        # when
        instance = generate_instance(input_line)
        # then
        self.assertIsInstance(instance, how_much_question)

    def test_generate_how_many_question_instance_accord_to_input(self):
        # given
        input_line = 'how many Credits is glob prok Silver ?'
        # when
        instance = generate_instance(input_line)
        # then
        self.assertIsInstance(instance, how_many_question)

    def test_generate_error_instance_accord_to_input(self):
        # given
        input_line = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'
        # when
        instance = generate_instance(input_line)
        # then
        self.assertIsInstance(instance, error)
