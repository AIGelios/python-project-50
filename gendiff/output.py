def formatted(value):
    if type(value) in [int, float, str]:
        return str(value)
    elif type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        raise Exception('ERROR: Unsupported data type')


def stylish(dict_difference):
    result = '{\n'
    for entry in dict_difference:
        key, old_value, new_value = entry.values()
        if old_value == new_value:
            result += f'    {key}: {formatted(old_value)}\n'
        else:
            if old_value != {None}:
                result += f'  - {key}: {formatted(old_value)}\n'
            if new_value != {None}:
                result += f'  + {key}: {formatted(new_value)}\n'
    result += '}'
    return result
