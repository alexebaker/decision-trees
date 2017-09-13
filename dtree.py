from __future__ import print_function
from __future__ import unicode_literals

from decision_tree import cli
from decision_tree import dtree
from decision_tree.id3 import ID3Tree


def main():
    cli_args = cli.parse_args()

    training_data = dtree.parse_data(cli_args.get('training_data'))
    testing_data = dtree.parse_data(cli_args.get('testing_data'))

    id3 = ID3Tree(data=training_data)

    classification = id3.classify_data(testing_data)
    dtree.save_classification(classification, cli_args.get('classification_file'))
    return


if __name__ == "__main__":
    main()
