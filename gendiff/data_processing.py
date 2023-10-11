def formatted(value):
    if type(value) in [int, float, str]:
        return str(value)
    elif type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        raise Exception('ERROR: Unsupported data type')


def dict_diff(dict1, dict2, no_key={None}):
    result = []
    for key in sorted(dict1 | dict2):
        old_value = dict1.get(key, no_key)
        new_value = dict2.get(key, no_key)
        cond1 = old_value == new_value
        cond2 = key in dict1 and not cond1
        cond3 = key in dict2 and not cond1
        result += [(' ', key, formatted(old_value))] if cond1 else []
        result += [('-', key, formatted(old_value))] if cond2 else []
        result += [('+', key, formatted(new_value))] if cond3 else []
    return result