from gendiff.output_formats.stylish import formatted, stylish
from tests.test_data_processing import flat_diff, nested_diff


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

flat_stylish = 'tests/fixtures/flat_stylish.txt'
nested_stylish = 'tests/fixtures/nested_stylish.txt'

def test_stylish():
    with open(flat_stylish) as file:
        example = file.read()
    assert stylish(flat_diff) == example

    with open(nested_stylish) as file:
        example = file.read()
    assert stylish(nested_diff) == example