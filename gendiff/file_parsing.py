import yaml
import json


def get_data_from_file(path: str) -> dict:
    '''get file path as a string and return data from file
    as a python dictionary object'''
    file_type = path.lower().split('.')[-1]
    if file_type in ('yaml', 'yml'):
        get_data = yaml.safe_load
    elif file_type in ('json',):
        get_data = json.load
    else:
        raise Exception('ERROR: Unsupported file type.')

    with open(path) as file:
        return get_data(file)
