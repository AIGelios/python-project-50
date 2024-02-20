from typing import Any
import json
from gendiff.data_processing import get_value_status


def get_formatted_value(value: Any):
    if type(value) is list:
        return make_data_for_dump(value)
    return value


def make_data_for_dump(dict_difference):
    result = {}
    for entry in dict_difference:
        status = get_value_status(entry)
        key = entry['key']
        old_value = entry['old_value']
        new_value = entry['new_value']
        match status:
            case 'added':
                result.update({key: {
                    'status': status,
                    'new_value': get_formatted_value(new_value),
                }})
            case 'removed':
                result.update({key: {
                    'status': status,
                    'old_value': get_formatted_value(old_value),
                }})
            case 'unchanged':
                result.update({key: get_formatted_value(old_value)})
            case 'updated':
                result.update({key: {
                    'status': status,
                    'old_value': get_formatted_value(old_value),
                    'new_value': get_formatted_value(new_value),
                }})
    return result


def make_json(data):
    return json.dumps(make_data_for_dump(data), indent=2)
