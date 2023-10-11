from gendiff.scripts.gendiff import generate_diff
# import gendiff.output_format.stylish as stylish


flat_json_1 = 'tests/fixtures/flat1.json'
flat_json_2 = 'tests/fixtures/flat2.json'
flat_yaml_1 = 'tests/fixtures/flat1.yaml'
flat_yaml_2 = 'tests/fixtures/flat2.yml'
dif_flat1_flat2_stylish = 'tests/fixtures/dif_flat1_flat2_stylish.txt'
dif_flat2_flat1_stylish = 'tests/fixtures/dif_flat2_flat1_stylish.txt'


def test_generate_diff():

    with open(dif_flat1_flat2_stylish) as file_1_2:
        dif_1_2 = file_1_2.read()
    assert generate_diff(flat_json_1, flat_json_2, 'stylish') == dif_1_2
    assert generate_diff(flat_yaml_1, flat_yaml_2, 'stylish') == dif_1_2

    with open(dif_flat2_flat1_stylish) as file_2_1:
        dif_2_1 = file_2_1.read()
    assert generate_diff(flat_json_2, flat_json_1, 'stylish') == dif_2_1
    assert generate_diff(flat_yaml_2, flat_yaml_1, 'stylish') == dif_2_1
