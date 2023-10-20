from gendiff import yaml
from gendiff.output_formats.json_output import make_data_for_dump


def dump_yaml(data):
    return yaml.safe_dump(data, explicit_start=True)


def make_yaml(data):
    return dump_yaml(make_data_for_dump(data))
