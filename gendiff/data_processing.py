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
    elif old_value == {None}:
        return 'added'
    elif new_value == {None}:
        return 'removed'
    else:
        return 'updated'


def dict_diff(old_dict, new_dict={}):
    new_dict = new_dict if new_dict else old_dict
    result = []
    for key in sorted(old_dict | new_dict):
        old_value = old_dict.get(key, {None})
        new_value = new_dict.get(key, {None})
        old_value, new_value = check_values(old_value, new_value)
        entry = {'key': key,
                 'old_value': old_value,
                 'new_value': new_value,
                 }
        result.append(entry)
    return result
