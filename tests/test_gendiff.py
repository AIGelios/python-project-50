from gendiff import generate_diff
from subprocess import check_output


help_file = 'tests/fixtures/help_output.txt'
flat_json_1 = 'tests/fixtures/flat1.json'
flat_json_2 = 'tests/fixtures/flat2.json'
flat_yaml_1 = 'tests/fixtures/flat1.yaml'
flat_yaml_2 = 'tests/fixtures/flat2.yml'
dif_flat1_flat2_stylish = 'tests/fixtures/dif_flat1_flat2_stylish.txt'
dif_flat2_flat1_stylish = 'tests/fixtures/dif_flat2_flat1_stylish.txt'
nested_json_1 = 'tests/fixtures/nested1.json'
nested_json_2 = 'tests/fixtures/nested2.json'
nested_yaml_1 = 'tests/fixtures/nested1.yml'
nested_yaml_2 = 'tests/fixtures/nested2.yaml'
dif_nes1_nes2_stylish = 'tests/fixtures/dif_nes1_nes2_stylish.txt'
dif_nes1_nes2_plain = 'tests/fixtures/dif_nes1_nes2_plain.txt'
dif_nes1_nes2_json = 'tests/fixtures/dif_nes1_nes2.json'
dif_nes1_nes2_yaml = 'tests/fixtures/dif_nes1_nes2.yml'


# generate_diff function test
def test_generate_diff():
    # flat json test
    with open(dif_flat1_flat2_stylish) as file:
        dif = file.read()
    assert generate_diff(flat_json_1, flat_json_2, 'stylish') == dif

    # flat yaml test
    with open(dif_flat2_flat1_stylish) as file:
        dif = file.read()
    assert generate_diff(flat_yaml_2, flat_yaml_1, 'stylish') == dif

    # nested json and yaml test (stylish output)
    with open(dif_nes1_nes2_stylish) as file:
        dif = file.read()
    assert generate_diff(nested_json_1, nested_yaml_2, 'stylish') == dif

    # nested json and yaml test (plain output)
    with open(dif_nes1_nes2_plain) as file:
        dif = file.read()
    assert generate_diff(nested_yaml_1, nested_json_2, 'plain') == dif

    # nested json and yaml test (json output):
    with open(dif_nes1_nes2_json) as file:
        dif = file.read()
    assert generate_diff(nested_json_1, nested_yaml_2, 'json') == dif

    # nested json and yaml test (json output):
    with open(dif_nes1_nes2_yaml) as file:
        dif = file.read()
    assert generate_diff(nested_json_1, nested_yaml_2, 'yaml') == dif

    # nested json test with wrong output format:
    try:
        generate_diff(nested_json_1, nested_json_2, 'bad_format')
        assert False
    except Exception:
        assert True


# main command line test
def test_cli():
    # gendiff -h output test
    with open(help_file) as file:
        example = file.read()
    output = check_output(
        ['gendiff', '-h'],
        text=True
    )
    assert output == example

    # flat json files dif output test
    with open(dif_flat1_flat2_stylish) as file:
        example = file.read()
    output = check_output(
        ['gendiff', flat_json_1, flat_json_2],
        text=True
    )
    assert output.rstrip() == example

    # flat yaml files dif output test
    with open(dif_flat2_flat1_stylish) as file:
        example = file.read()
    output = check_output(
        ['gendiff', flat_yaml_2, flat_yaml_1, '-f', 'stylish'],
        text=True
    )
    assert output.rstrip() == example

    # nested json files output test (default 'stylish' format)
    with open(dif_nes1_nes2_stylish) as file:
        example = file.read()
    output = check_output(
        ['gendiff', nested_json_1, nested_json_2],
        text=True,
    )
    assert output.rstrip() == example

    # nested json files output test ('plain' format)
    with open(dif_nes1_nes2_plain) as file:
        example = file.read()
    output = check_output(
        ['gendiff', '-f', 'plain', nested_json_1, nested_json_2],
        text=True,
    )
    assert output.rstrip() == example

    # nested json files output test ('json' format)
    with open(dif_nes1_nes2_json) as file:
        example = file.read()
    output = check_output(
        ['gendiff', '-f', 'json', nested_json_1, nested_json_2],
        text=True,
    )
    assert output.rstrip() == example

    # nested json files output test ('yaml' format)
    with open(dif_nes1_nes2_yaml) as file:
        example = file.read()
    output = check_output(
        ['gendiff', '-f', 'yaml', nested_json_1, nested_json_2],
        universal_newlines=True,
    )
    assert output.rstrip() == example
