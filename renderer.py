#!/usr/bin/env python3

"""
This script will generate a 'user-data.yml' file from the a template.
It receives a configuration file that can be a YAML or python configuration
file that hols the option to configure.

The options and configurations are defined in 'samples-user-data.cfg'.

Example
-------

python renderer.py --config-file user-data.cfg

Usage
-----

usage: renderer.py [-h] [--config-file CONFIG_FILE] [--out-dir OUT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Configuration file name, absolute path, should be a python configuration file or a yaml (default: sample-user-data.cfg)
  --out-dir OUT_DIR     Directory to store the generated user-data.yml (default: .)
"""


import argparse
import yaml
import os
from configparser import ConfigParser, ParsingError
from jinja2 import Environment, FileSystemLoader

USER_DATA_FILE_NAME = 'user-data.yml'
DEFAULT_OUTPUT_DIR = '.'


def load_config(config_file):
    config = None
    with open(config_file) as _file:
        try:
            config = yaml.load(_file, Loader=yaml.FullLoader)
        except yaml.parser.ParserError:
            try:
                _file.seek(0)
                parser = ConfigParser()
                parser.read_file(_file)
                config = parser._sections  # pylint:disable=protected-access
            except ParsingError:
                # pylint: disable=raise-missing-from
                raise BadParameter("Cannot parse config file '{_file.filename}'")
    return config


def main(config_file, out_dir):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template(USER_DATA_FILE_NAME + '.j2')

    config = load_config(config_file)
    user_data = template.render(config,zip=zip)

    dest = os.path.join(out_dir, USER_DATA_FILE_NAME)
    with open(dest, "w") as _file:
        _file.write(user_data)


PARSER = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
PARSER.add_argument('--config-file',
                    type=str,
                    default='sample-user-data.cfg',
                    help='''Configuration file name, absolute path, should be
                            a python configuration file or a yaml''')
PARSER.add_argument('--out-dir',
                    type=str,
                    default=DEFAULT_OUTPUT_DIR,
                    help='Directory to store the generated user-data.yml')

if __name__ == '__main__':
    args = PARSER.parse_args()
    main(args.config_file, args.out_dir)
