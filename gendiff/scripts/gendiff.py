from argparse import ArgumentParser
from gendiff.file_parsing import get_data
from gendiff.data_processing import dict_diff
import gendiff.output_format.stylish as stylish


def get_arguments():
    parser_info = 'Compares two configuration files and shows a difference.'
    parser = ArgumentParser(description=parser_info)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    return parser.parse_args()


def generate_diff(path_1, path_2, format):
    format_module = {'stylish': stylish}[format]
    data_1 = get_data(path_1)
    data_2 = get_data(path_2)
    diff = dict_diff(data_1, data_2)
    return format_module.output(diff)


def main():
    args = get_arguments()
    path_1 = args.first_file
    path_2 = args.second_file
    format = args.format
    result = generate_diff(path_1, path_2, format)
    print(result)


if __name__ == '__main__':
    main()
