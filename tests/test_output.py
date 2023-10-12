from gendiff.output import formatted, stylish


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


def test_stylish():
    no_value = {None}

    changes = [{'key': 'a', 'old_value': 1, 'new_value': 1},
               {'key': 'b', 'old_value': 1.5, 'new_value': no_value},
               {'key': 'c', 'old_value': no_value, 'new_value': 'abc'},
               {'key': 'd', 'old_value': True, 'new_value': False}]

    with open('tests/fixtures/flat_stylish.txt') as file:
        example = file.read()
    assert stylish(changes) ==  example
