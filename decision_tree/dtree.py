from __future__ import print_function
from __future__ import unicode_literals

import sys
import math

from decision_tree.id3 import ID3Tree


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

def entropy(p_value):
    total=0
    for p in p_value:
      if p!=0:
          total-= p*math.log(p)
    return total

def dna_p_value(dna_data):
    """Calculates probabilty of each of the 3 classes for a set of strands
    """
    ei_count=0
    ie_count=0
    n_count=0
    total=0
    for dna in dna_data:
       total+=1
       if dna['class']=='IE':
            ie_count+=1
       elif dna['class']=='EI':
            ei_count+=1
       else:
            n_count+=1
    try:
       return (ei_count / total, ie_count / total, n_count / total)
    except ZeroDivisionError:
       print ("empty list cannot produce probability")


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
    data = []
    for line in data_file.readlines():
        parts = line.split(',')
        if len(parts) == 2:
            idx, attrs = parts
            data.append({'id': idx,
                         'attrs': attrs.strip('\r\n')})
        elif len(parts) == 3:
            idx, attrs, cls = parts
            data.append({'id': idx,
                         'attrs': attrs,
                         'class': cls.strip('\r\n')})
        else:
            print('Data file is formatted incorrectly.', file=sys.stderr)
            sys.exit(1)
    return data


def save_classification(classification, classification_file):
    """Saves the classification from the ID3 algorithm to a file.

    :type classification: list
    :param classification: The classification output from the ID3 algorithm for the testing data.

    :type classification_file: File Object
    :param classification_file: File to write the classification to.
    """
    print('id', 'class', file=classification_file, sep=',')
    for item in classification:
        idx, cls = item.values()
        print(idx, cls, file=classification_file, sep=',')
    return
