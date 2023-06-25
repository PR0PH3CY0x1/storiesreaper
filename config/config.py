from json import load


def read_data(filepath):
    with open(filepath, 'r') as file:
        data = load(file)

    return data
