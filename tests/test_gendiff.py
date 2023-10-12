from gendiff.scripts.gendiff import generate_diff
from subprocess import check_output
# import gendiff.output_format.stylish as stylish


flat_json_1 = 'tests/fixtures/flat1.json'
flat_json_2 = 'tests/fixtures/flat2.json'
flat_yaml_1 = 'tests/fixtures/flat1.yaml'
flat_yaml_2 = 'tests/fixtures/flat2.yml'
dif_flat1_flat2_stylish = 'tests/fixtures/dif_flat1_flat2_stylish.txt'
dif_flat2_flat1_stylish = 'tests/fixtures/dif_flat2_flat1_stylish.txt'
help_output = 'tests/fixtures/help_output.txt'


def test_generate_diff():

    with open(dif_flat1_flat2_stylish) as file_1_2:
        dif_1_2 = file_1_2.read()
    assert generate_diff(flat_json_1, flat_json_2, 'stylish') == dif_1_2
    assert generate_diff(flat_yaml_1, flat_yaml_2, 'stylish') == dif_1_2

    with open(dif_flat2_flat1_stylish) as file_2_1:
        dif_2_1 = file_2_1.read()
    assert generate_diff(flat_json_2, flat_json_1, 'stylish') == dif_2_1
    assert generate_diff(flat_yaml_2, flat_yaml_1, 'stylish') == dif_2_1


def test_cli():
    with open(help_output) as file:
        sample = file.read()
    output = check_output(['gendiff', '-h'], universal_newlines=True)
    assert output == sample

    with open(dif_flat1_flat2_stylish) as file:
        sample = file.read() + '\n'
    output = check_output(['gendiff', flat_json_1, flat_json_2],
                          universal_newlines=True)
    assert output == sample

    with open(dif_flat2_flat1_stylish) as file:
        sample = file.read() + '\n'
    output = check_output(['gendiff', flat_yaml_2, flat_yaml_1,
                           '-f', 'stylish'], universal_newlines=True)
    assert output == sample
