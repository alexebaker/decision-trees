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


def chi_square(e_values, o_values, dof, alpha):
    x2= chi_sq_dist(dof, alpha)
    xc2=0
    for i in range(0,dof+1):
      xc2+= ((o_values[i]- e_values[i])**2)/e_values[i]
    print(x2)
    print(xc2)
    #reject null hypothesis
    if xc2>x2:
      return False
    else:
      return True

def chi_sq_dist(dof, alpha):
   dof2 =[
     {'alpha': 0.20 ,'crit_val': 3.219},
     {'alpha': 0.10 ,'crit_val': 4.605},
     {'alpha': 0.05 ,'crit_val': 5.991},
     {'alpha': 0.025 ,'crit_val': 7.378},
     {'alpha': 0.02 ,'crit_val': 7.824},
     {'alpha': 0.01 ,'crit_val': 9.210},
     {'alpha': 0.005 ,'crit_val': 10.597},
     {'alpha': 0.002 ,'crit_val': 12.429},
     {'alpha': 0.001 ,'crit_val': 13.816}
   ]
   dof3 =[
     {'alpha': 0.20 ,'crit_val': 4.642},
     {'alpha': 0.10 ,'crit_val': 6.251},
     {'alpha': 0.05 ,'crit_val': 7.815},
     {'alpha': 0.025 ,'crit_val': 9.348},
     {'alpha': 0.02 ,'crit_val': 9.837},
     {'alpha': 0.01 ,'crit_val': 11.345},
     {'alpha': 0.005 ,'crit_val': 12.838},
     {'alpha': 0.002 ,'crit_val': 14.796},
     {'alpha': 0.001 ,'crit_val': 16.266}
   ]
   dof7 =[
     {'alpha': 0.20 ,'crit_val': 9.803},
     {'alpha': 0.10 ,'crit_val': 12.017},
     {'alpha': 0.05 ,'crit_val': 14.067},
     {'alpha': 0.025 ,'crit_val': 16.013},
     {'alpha': 0.02 ,'crit_val': 16.622},
     {'alpha': 0.01 ,'crit_val': 18.475},
     {'alpha': 0.005 ,'crit_val': 20.278},
     {'alpha': 0.002 ,'crit_val': 22.601},
     {'alpha': 0.001 ,'crit_val': 24.322}
   ]
   dofX = []
   if dof==2:
     dofX=dof2
   elif dof==3:
     dofX=dof3
   elif dof==7:
     dofX=dof7
   else:
     print ("Unsupported degree of freedom used!")
     return 0
   for cv in dofX:
     if cv['alpha']==alpha:
       return cv['crit_val']

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
