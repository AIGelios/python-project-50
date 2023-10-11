from gendiff.data_processing import formatted, dict_diff


def test_formatted():
    assert formatted(1) == '1'
    assert formatted(1.5) == '1.5'
    assert formatted('abc') == 'abc'
    assert formatted(True) == 'true'
    assert formatted(False) == 'false'
    assert formatted(None) == 'null'
    try:
        x = formatted(set())
    except:
        pass


def test_dict_diff():
    dict_1 = {'a': None, 'b': True, 'aa': 1, 'd': 1.5}
    dict_2 = {'a': None, 'c': 'xyz', 'd': 1.5, 'b': False}
    diff = [(' ', 'a', 'null'),
            ('-', 'aa', '1'),
            ('-', 'b', 'true'),
            ('+', 'b', 'false'),
            ('+', 'c', 'xyz'),
            (' ', 'd', '1.5')]
    assert dict_diff(dict_1, dict_2) == diff
