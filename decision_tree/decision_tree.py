from __future__ import print_function
from __future__ import unicode_literals

def id3(data):
    """Run the ID3 Algorithm with the given data to create a decision tree.

    :type data: ?
    :param data: Data read in from the data file to create the decision tree from.

    :rtype: ?
    :returns: A decision tree create by running the data through the ID3 algorithm.
    """
    return


def gini_index():
    """Calculates the Gini Index for the given parameters.

    :rtype: ?
    :returns: The calculated Gini Index for the given parameters.
    """
    return


def info_gain():
    """Calculates the information gain for the given parameters.

    :rtype: ?
    :returns: The calculated information gain for the given parameters.
    """
    return


def chi_square():
    """Calculates the chi square for the given parameters.

    :rtype: ?
    :returns: The calculated chi square for the given parameters.
    """
    return


def parse_data(data_file):
    """Parses the data out of the data file and into a format used by the ID3 algorithm.

    :type data_file: File Object
    :param data_file: A file object from the cli to parse into a data structure.

    :rtype: ?
    :returns: A data structure with the parsed data from the data file.
    """
    for line in data_file.readlines():
        print(line)
    return
