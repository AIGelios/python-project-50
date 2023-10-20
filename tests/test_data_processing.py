from gendiff.data_processing import dict_diff, NO_ITEM


flat_dict_1 = {'a': None, 'b': True, 'aa': 1, 'd': 1.5}
flat_dict_2 = {'a': None, 'c': 'xyz', 'd': 1.5, 'b': False}
flat_diff = [
    {'key': 'a', 'old_value': None, 'new_value': None},
    {'key': 'aa', 'old_value': 1, 'new_value': NO_ITEM},
    {'key': 'b', 'old_value': True, 'new_value': False},
    {'key': 'c', 'old_value': NO_ITEM, 'new_value': 'xyz'},
    {'key': 'd', 'old_value': 1.5, 'new_value': 1.5},
]

nested_dict_1 = {'a': {'b': 1, 'c': True}, 'd': 'no'}
nested_dict_2 = {'a': {'b': 2, 'c': False}, 'd': 'yes'}
nested_diff = [
    {'key': 'a',
     'old_value': [
         {'key': 'b', 'old_value': 1, 'new_value': 2},
         {'key': 'c', 'old_value': True, 'new_value': False},
        ],
     'new_value': [
         {'key': 'b', 'old_value': 1, 'new_value': 2},
         {'key': 'c', 'old_value': True, 'new_value': False},
        ]
     },
    {'key': 'd',
     'old_value': 'no',
     'new_value': 'yes'
     }
]


def test_dict_diff():
    assert dict_diff(flat_dict_1, flat_dict_2) == flat_diff
    assert dict_diff(nested_dict_1, nested_dict_2) == nested_diff
