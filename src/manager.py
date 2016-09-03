import os


def read_file(filename):
    if not os.path.isfile(filename):
        return None

    file_content = ''
    with open(filename, 'r') as fd:
        for line in fd:
            file_content += line

    return file_content
