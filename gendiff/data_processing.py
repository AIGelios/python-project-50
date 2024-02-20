from typing import Any


NO_ITEM = {None}


def is_dict(data: Any) -> bool:
    '''return True if argument type is dict, otherwise False'''
    return isinstance(data, dict)


def check_values(value1: Any, value2: Any) -> tuple:
    if is_dict(value1) and is_dict(value2):
        return (get_dict_diff(value1, value2), get_dict_diff(value1, value2))
    elif is_dict(value1):
        return (get_dict_diff(value1), value2)
    elif is_dict(value2):
        return (value1, get_dict_diff(value2))
    else:
        return (value1, value2)


def get_value_status(entry: dict) -> str:
    '''Take diff entry (type dict) and return status of value'''
    old_value = entry['old_value']
    new_value = entry['new_value']
    if old_value == new_value:
        return 'unchanged'
    elif old_value == NO_ITEM:
        return 'added'
    elif new_value == NO_ITEM:
        return 'removed'
    else:
        return 'updated'


def get_dict_diff(old_dict: dict, new_dict: dict = {}) -> list:
    '''Take 2 dicts and return data of differrence between it
    (keys added, keys removed, values left/updated)'''
    new_dict = new_dict if new_dict else old_dict
    result = []
    for key in sorted(old_dict | new_dict):
        old_value = old_dict.get(key, NO_ITEM)
        new_value = new_dict.get(key, NO_ITEM)
        old_value, new_value = check_values(old_value, new_value)
        entry = {
            'key': key,
            'old_value': old_value,
            'new_value': new_value,
        }
        result.append(entry)
    return result
