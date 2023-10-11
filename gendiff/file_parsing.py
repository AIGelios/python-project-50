import yaml
import json


def get_data(path):
    file_type = path.lower().split('.')[-1]
    if file_type in ('yaml', 'yml'):
        get_data = yaml.safe_load
    elif file_type == 'json':
        get_data = json.load
    else:
        raise Exception('ERROR: Unsupported file type.')

    with open(path) as file:
        return get_data(file)
