def dict_diff(old_dict, new_dict):
    def is_dict(data):
        return isinstance(data, dict)

    result = []
    for key in sorted(old_dict | new_dict):
        old_value = old_dict.get(key, {None})
        new_value = new_dict.get(key, {None})
        if is_dict(old_value) and is_dict(new_value):
            old_value = new_value = dict_diff(old_value, new_value)
        else:
            if is_dict(old_value):
                old_value = dict_diff(old_value, old_value)
            if is_dict(new_value):
                new_value = dict_diff(new_value, new_value)
        entry = {'key': key,
                 'old_value': old_value,
                 'new_value': new_value,
                 }
        result.append(entry)
    return result
