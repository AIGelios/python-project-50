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
        cond1, cond2 = key in dict1, key in dict2
        old_value = dict1[key] if cond1 else no_key
        new_value = dict2[key] if cond2 else no_key
        if key in dict1:
            result += [('-', key, formatted(old_value))]
        if key in dict2:
            result += [('+', key, formatted(new_value))]
        if old_value == new_value:
            result = result[:-2] + [(' ', key, formatted(old_value))]
    return result