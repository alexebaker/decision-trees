from __future__ import print_function
from __future__ import unicode_literals

from decision_tree import cli
from decision_tree import dtree
from decision_tree.id3 import ID3Tree


def main():
    """Main entry point to the decision tree."""
    # Parse the command line arguments
    cli_args = cli.parse_args()

    # Parse the training and testing data file given from the cli arguments
    training_data = dtree.parse_data(cli_args.get('training_data'))
    testing_data = dtree.parse_data(cli_args.get('testing_data'))

    # This creates and ID3Tree object and builds a decision tree based on the input data
    id3 = ID3Tree(dna_data=training_data,
                  use_gini_index=cli_args.get('gini_index'),
                  alpha=cli_args.get('alpha'))

    # Use the build decision tree to classify the data given in the testing data file
    classification = id3.classify_data(testing_data)

    # Write the classification to a file for submission
    dtree.save_classification(classification, cli_args.get('classification_file'))
    return


if __name__ == "__main__":
    main()
