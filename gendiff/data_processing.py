def dict_diff(old_dict, new_dict):
    result = []
    for key in sorted(old_dict | new_dict):
        entry = {'key': key,
                 'old_value': old_dict.get(key, {None}),
                 'new_value': new_dict.get(key, {None}),
                 }
        result.append(entry)
    return result
