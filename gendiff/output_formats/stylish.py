from gendiff.data_processing import value_status


def formatted(value, offset=''):
    if type(value) in [int, float, str]:
        return str(value)
    elif type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif type(value) is list:
        return make_stylish(value, offset + ' ' * 4)
    else:
        raise Exception('ERROR: Unsupported data type')


def make_stylish(dict_difference, offset=''):
    def unchanged(key, value, offset):
        return f'{offset}    {key}: {formatted(value, offset)}\n'

    def removed(key, value, offset):
        return f'{offset}  - {key}: {formatted(value, offset)}\n'

    def added(key, value, offset):
        return f'{offset}  + {key}: {formatted(value, offset)}\n'

    def updated(key, old_value, new_value, offset):
        old_args = key, old_value, offset
        new_args = key, new_value, offset
        return removed(*old_args) + added(*new_args)

    result = '{\n'
    for entry in dict_difference:
        key = entry['key']
        old_value = entry['old_value']
        new_value = entry['new_value']
        status = value_status(entry)
        match status:
            case 'unchanged':
                result += unchanged(key, old_value, offset)
            case 'removed':
                result += removed(key, old_value, offset)
            case 'added':
                result += added(key, new_value, offset)
            case 'updated':
                result += updated(key, old_value, new_value, offset)
    result += offset + '}'
    return result
