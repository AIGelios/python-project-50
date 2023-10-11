def output(changes):
    result = '{\n'
    for entry in changes:
        action, key, value = entry
        result += f'  {action} {key}: {value}\n'
    result += '}'
    return result
