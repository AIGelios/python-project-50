from argparse import ArgumentParser
from gendiff.file_parsing import get_data_from_file
from gendiff.data_processing import get_dict_diff
from gendiff.output_formats import (
    make_stylish, make_plain, make_json, make_yaml
)


ABOUT_APP = 'Compares two configuration files and shows a difference.'


def get_arguments():
    parser_info = ABOUT_APP
    parser = ArgumentParser(description=parser_info)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', metavar='FORMAT',
        help='set format of output',
        default='stylish'
    )
    return parser.parse_args()


def generate_diff(path_1: str, path_2: str, format: str = 'stylish') -> str:
    make_output = {
        'stylish': make_stylish,
        'plain': make_plain,
        'json': make_json,
        'yaml': make_yaml
    }.get(format)
    if make_output is None:
        raise Exception('ERROR: Unknown output format')
    data_1 = get_data_from_file(path_1)
    data_2 = get_data_from_file(path_2)
    diff = get_dict_diff(data_1, data_2)
    return make_output(diff).rstrip()


def main():
    args = get_arguments()
    path_1 = args.first_file
    path_2 = args.second_file
    format = args.format
    result = generate_diff(path_1, path_2, format)
    print(result)


if __name__ == '__main__':
    main()
