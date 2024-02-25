# GENDIFF
Welcome to the Gendiff console utility.
This utility shows a difference between 2 configuration files.
It supports JSON (*.json) and YAML (*.yaml, *.yml) formats of config files.

### Hexlet and CodeClimate tests and linter status:
[![Actions Status](https://github.com/AIGelios/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AIGelios/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/24b07c2c9d3dbe3b4547/maintainability)](https://codeclimate.com/github/AIGelios/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/24b07c2c9d3dbe3b4547/test_coverage)](https://codeclimate.com/github/AIGelios/python-project-50/test_coverage)

### System requirements:
1. Linux
2. Python 3.10+
3. Poetry

### Installation:
1. Clone the repository with command: ```git clone git@github.com:AIGelios/python-project-50.git```
2. Choose a working directory with command ```cd python-project-50/```
3. Make installation with command ```make full-install```

### Usage:
Use this command in your terminal:
```gendiff file_path_1 file_path_2 [--option]```

available options:
-h, --help : information about utility, available commands, etc.
-f --format : format of files difference output. Available formats: 'stylish' (default), 'plane', 'json', 'yaml'.

Command examples:
```gendiff file1.json file2.json```
```gendiff file2.yaml file1.yml -f stylish```
```gendiff file3.json file4.json --format plain```
```gendiff -h```

### HOW IT WORKS: i'll show you in assiinema:
[![asciicast](https://asciinema.org/a/641475.svg)](https://asciinema.org/a/641475)

### Uninstallation:
```make package-uninstall```
and then remove the directory of thew project with ```rm -r```




