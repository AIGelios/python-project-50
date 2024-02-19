import yaml
from gendiff.output_formats.json_output import make_data_for_dump


def make_yaml(data):
    return yaml.safe_dump(make_data_for_dump(data), explicit_start=True)
