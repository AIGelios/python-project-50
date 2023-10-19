from yaml import safe_dump
from gendiff.output_formats.json import make_data_for_dump


def make_yaml(data):
    return safe_dump(make_data_for_dump(data), explicit_start=True)
