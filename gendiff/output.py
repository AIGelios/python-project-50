def formatted(value):
    if type(value) in [int, float, str]:
        return str(value)
    elif type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        raise Exception('ERROR: Unsupported data type')


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


def stylish(dict_difference):
    result = '{\n'
    for entry in dict_difference:
        key, old_value, new_value = entry.values()
        status = value_status(entry)
        match status:
            case 'unchanged':
                result += f'    {key}: {formatted(old_value)}\n'
            case 'removed':
                result += f'  - {key}: {formatted(old_value)}\n'
            case 'added':
                result += f'  + {key}: {formatted(new_value)}\n'
            case 'updated':
                result += f'  - {key}: {formatted(old_value)}\n'
                result += f'  + {key}: {formatted(new_value)}\n'
    result += '}'
    return result
