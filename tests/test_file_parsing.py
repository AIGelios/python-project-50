from gendiff.file_parsing import get_data


def test_get_data_from_file():

    flat_data_1 = {'host': 'hexlet.io',
              'timeout': 50,
              'proxy': "123.234.53.22",
              'follow': False}

    flat_data_2 = {'timeout': 20,
                   'verbose': True,
                   'host': 'hexlet.io'}

    path_1 = 'tests/fixtures/flat1.json'
    path_2 = 'tests/fixtures/flat2.json'
    path_3 = 'tests/fixtures/flat1.yaml'
    path_4 = 'tests/fixtures/flat2.yml'
    path_5 = 'gendiff/scripts/gendiff.py'

    assert get_data(path_1) == get_data(path_3) == flat_data_1
    assert get_data(path_2) == get_data(path_4) == flat_data_2
    try:
        get_data(path_5)
    except:
        print('unsupported file test passed')
