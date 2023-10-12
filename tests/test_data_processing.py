from gendiff.data_processing import dict_diff


def test_dict_diff():
    dict_1 = {'a': None, 'b': True, 'aa': 1, 'd': 1.5}
    dict_2 = {'a': None, 'c': 'xyz', 'd': 1.5, 'b': False}
    no_value = {None}
    diff = [{'key': 'a', 'old_value': None, 'new_value': None},
            {'key': 'aa', 'old_value': 1, 'new_value': no_value},
            {'key': 'b', 'old_value': True, 'new_value': False},
            {'key': 'c', 'old_value': no_value, 'new_value': 'xyz'},
            {'key': 'd', 'old_value': 1.5, 'new_value': 1.5}]
    assert dict_diff(dict_1, dict_2) == diff
