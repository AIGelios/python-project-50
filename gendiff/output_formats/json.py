from json import dumps as dump_json
from gendiff.data_processing import value_status


def formatted(value):
    if type(value) is list:
        return make_data_for_dump(value)
    return value


def make_data_for_dump(dict_difference):
    result = {}
    for entry in dict_difference:
        status = value_status(entry)
        key = entry['key']
        old_value = entry['old_value']
        new_value = entry['new_value']
        match status:
            case 'added':
                result |= {key: {'status': status,
                                 'new_value': formatted(new_value)}}
            case 'removed':
                result |= {key: {'status': status,
                                 'old_value': formatted(old_value)}}
            case 'unchanged':
                result |= {key: formatted(old_value)}
            case 'updated':
                result |= {key: {'status': status,
                                 'old_value': formatted(old_value),
                                 'new_value': formatted(new_value)}}
    return result


def make_json(data):
    return dump_json(make_data_for_dump(data), indent=2)
