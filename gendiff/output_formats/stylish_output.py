from gendiff.data_processing import value_status


def format_value(value, offset=''):
    if type(value) in [int, float, str]:
        return str(value)
    elif type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif type(value) is list:
        return make_stylish(value, offset + ' ' * 4)


def make_stylish(dict_difference, offset=''):
    def unchanged(key, value, offset):
        return f'{offset}    {key}: {format_value(value, offset)}\n'

    def removed(key, value, offset):
        return f'{offset}  - {key}: {format_value(value, offset)}\n'

    def added(key, value, offset):
        return f'{offset}  + {key}: {format_value(value, offset)}\n'

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


'''
def make_stylish(diff: dict, offset='') -> str:
    result = '{\n'
    for key in sorted(diff):
        status = diff[key]['status']
        match status:
            case 'unchanged':
                value = diff[key]['old_value']
                result += f'{offset}    {key}: {format_value(value)}\n'
            case 'removed':
                value = diff[key]['old_value']
                result += f'{offset}  - {key}: {format_value(value)}\n'
            case 'added':
                value = diff[key]['new_value']
                result += f'{offset}  + {key}: {format_value(value)}\n'
            case 'updated':
                old_value = diff[key]['old_value']
                new_value = diff[key]['new_value']
                result += f'{offset}  - {key}: {format_value(old_value)}\n'
                result += f'{offset}  + {key}: {format_value(new_value)}\n'
            case 'node':
                result += make_stylish(diff[key]['children'], offset + '    ')
    return result + offset + '}'
'''
