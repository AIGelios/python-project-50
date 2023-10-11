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
        cond1 = dict1.get(key, no_key) == dict2.get(key, no_key)
        cond2 = key in dict1 and not cond1
        cond3 = key in dict2 and not cond1
        if cond1:
            result.append((' ', key, formatted(dict1[key])))
        if cond2:
            result.append(('-', key, formatted(dict1[key])))
        if cond3:
            result.append(('+', key, formatted(dict2[key])))
    return result
