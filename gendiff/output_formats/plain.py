from gendiff.data_processing import value_status


def formatted(value):
    if type(value) in [bool, int, float]:
        return str(value).lower()
    elif type(value) is str:
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif type(value) is list:
        return '[complex value]'
    else:
        raise Exception('ERROR: Unsupported data type')


def make_plain(dict_difference, prefix=''):
    result = ''
    for entry in dict_difference:
        key = entry['key']
        old_value = entry['old_value']
        new_value = entry['new_value']
        status = value_status(entry)
        match status:
            case 'added':
                result += f"Property '{prefix}{key}' was added with "
                result += f"value: {formatted(new_value)}\n"
            case 'removed':
                result += f"Property '{prefix}{key}' was removed\n"
            case 'updated':
                result += f"Property '{prefix}{key}' was updated. "
                result += f"From {formatted(old_value)} "
                result += f"to {formatted(new_value)}\n"
            case 'unchanged':
                if type(old_value) is list:
                    result += make_plain(old_value, prefix + f'{key}.')
    return result
