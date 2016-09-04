import os
import file


def write_file(output_data):
    with open(os.path.join(file, 'data/output.txt'), 'a') as fd:
        fd.write(output_data + '\n')


def print_to_console(output_data):
    print(output_data)
    return True


def output(output_data):
    return print_to_console(output_data)
