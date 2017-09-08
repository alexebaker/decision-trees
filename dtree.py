from __future__ import print_function
from __future__ import unicode_literals

from decision_tree import cli
from decision_tree import decision_tree


def main():
    cli_args = cli.parse_args()
    data = decision_tree.parse_data(cli_args.get('data_file'))
    return


if __name__ == "__main__":
    main()
