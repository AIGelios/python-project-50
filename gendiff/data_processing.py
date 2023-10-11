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
        if key in dict1:
            result.append(('-', key, formatted(dict1[key])))
        if key in dict2:
            result.append(('+', key, formatted(dict2[key])))
        old_value = dict1.get(key, no_key)
        new_value = dict2.get(key, no_key)
        if old_value == new_value:
            del result[-2:]
            result.append((' ', key, formatted(dict1[key])))
    return result
