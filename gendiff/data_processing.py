NO_ITEM = {None}


def is_dict(data):
    return isinstance(data, dict)


def check_values(value1, value2):
    if is_dict(value1) and is_dict(value2):
        return (dict_diff(value1, value2), dict_diff(value1, value2))
    elif is_dict(value1):
        return (dict_diff(value1), value2)
    elif is_dict(value2):
        return (value1, dict_diff(value2))
    else:
        return value1, value2


def value_status(entry):
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


def dict_diff(old_dict, new_dict={}):
    new_dict = new_dict if new_dict else old_dict
    result = []
    for key in sorted(old_dict | new_dict):
        old_value = old_dict.get(key, NO_ITEM)
        new_value = new_dict.get(key, NO_ITEM)
        old_value, new_value = check_values(old_value, new_value)
        entry = {'key': key,
                 'old_value': old_value,
                 'new_value': new_value,
                 }
        result.append(entry)
    return result


'''
# refactoring
def get_status(dict_1: dict, dict_2: dict, key: str) -> str:
    old_value = dict_1.get(key, NO_ITEM)
    new_value = dict_2.get(key, NO_ITEM)
    if type(old_value) is type(new_value) is dict:
        return 'node'
    elif old_value == new_value:
        return 'unchanged'
    elif old_value == NO_ITEM:
        return 'added'
    elif new_value == NO_ITEM:
        return 'removed'
    else:
        return 'updated'


def make_diff_entry(dict_1: dict, dict_2: dict, key: str) -> dict:
    status = get_status(dict_1, dict_2, key)
    entry = {key: {'status': status}}
    match status:
        case 'removed' | 'unchanged':
            entry[key]['old_value'] = dict_1[key]
        case 'added':
            entry[key]['new_value'] = dict_2[key]
        case 'updated':
            entry[key]['old_value'] = dict_1[key]
            entry[key]['new_value'] = dict_2[key]
        case 'node':
            entry[key]['children'] = dict_diff_2(dict_1[key], dict_2[key])
    return entry


def dict_diff_2(old_dict: dict, new_dict: dict) -> dict:
    result = {}
    for key in sorted(old_dict | new_dict):
        result |= make_diff_entry(old_dict, new_dict, key)
    return result
'''
