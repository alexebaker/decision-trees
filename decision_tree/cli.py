from __future__ import print_function
from __future__ import unicode_literals

import argparse


def parse_args():
    """Parse CLI arguments."""

    # argument parser object
    parser = argparse.ArgumentParser(
        description='Creates decision trees based on a given data file.')

    # Add arguments to the parser
    parser.add_argument(
        '--data-file',
        type=argparse.FileType(mode='r'),
        help='Path to the data file to use.')

    return vars(parser.parse_args())
