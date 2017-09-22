from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import math


def gini_value(dna_data):
    """takes the probabilty of each classification and multiplies them together"""
    p_values = dna_p_value(dna_data)
    gini_value = 1
    if not p_values:
        return 0
    else:
        for p in p_values:
            gini_value *= p
    return gini_value


def gini_gain(dna_data, values, attr):
    subset = get_subset2(dna_data, values, attr)
    gain = 0
    if subset:
        gain = gini_value(dna_data) - gini_value(subset)
    return gain


def is_same_class(dna_data):
    """Returns the class of the data if all the data shares the same class."""
    clses = [dna['class'] for dna in dna_data]
    return clses.count(clses[0]) == len(clses)


def get_class(dna_data):
    cls = ''
    class_count = dna_count_class(dna_data)
    max_count = max(class_count)
    if class_count[0] is max_count:
        cls = 'EI'
    elif class_count[1] is max_count:
        cls = 'IE'
    else:
        cls = 'N'
    return cls


def get_subset2(dna_data, value, attr):
    """Gets a subset of the data where attr has the given value."""
    subset = []
    for dna in dna_data:
        if dna['attrs'][attr] == value:
            subset.append(dna)
    return subset


def get_subset2(dna_data, value, attr):
    """Gets a subset of the data where attr has the given value."""
    subset = []
    for dna in dna_data:
        if dna['attrs'][attr] == value:
            subset.append(dna)
        elif dna['attrs'][attr] == 'D':
            if any([value == 'A', value == 'G', value == 'T']):
                subset.append(dna)
        elif dna['attrs'][attr] == 'N':
            subset.append(dna)
        elif dna['attrs'][attr] == 'S':
            if any([value == 'C', value == 'G']):
                subset.append(dna)
        elif dna['attrs'][attr] == 'R':
            if any([value == 'A', value == 'G']):
                subset.append(dna)
    return subset


def info_gain(dna_data, values, attr):
    """Calculates the information gain for the given parameters.

    :rtype: float
    :returns: The calculated information gain for the given parameters.
    """
    sum_total = 0
    for value in values:
        subset = get_subset2(dna_data, value, attr)
        if subset:
            sum_total += (len(subset) / len(dna_data)) * entropy(subset)

    return entropy(dna_data) - sum_total


def dna_p_value(dna_data):
    """Calculates probabilty of each of the 3 classes for a set of strands
    """
    ei_count = 0
    ie_count = 0
    n_count = 0
    total = 0
    for dna in dna_data:
        total += 1
        if dna['class'] == 'IE':
            ie_count += 1
        elif dna['class'] == 'EI':
            ei_count += 1
        else:
            n_count += 1
    try:
        return (ei_count/total, ie_count/total, n_count/total)
    except ZeroDivisionError:
        print ("empty list cannot produce probability")


def dna_count_class(dna_data):
    """counts the number of each class and returns them in this order - ei, ie
    and n.
    """
    ei_count = 0
    ie_count = 0
    n_count = 0
    for dna in dna_data:
        if dna['class'] == 'IE':
            ie_count += 1
        elif dna['class'] == 'EI':
            ei_count += 1
        else:
            n_count += 1
    return (ei_count, ie_count, n_count)


def entropy(dna_data):
    p_values = dna_p_value(dna_data)

    total = 0
    for p in p_values:
        if p != 0:
            total -= p * math.log(p, 2)
    return total


def rej_null_hyp(pNode, dof, alpha):
    p_values = dna_p_value(pNode.dna_data)
    e_count = []
    r_count = []
    for child in pNode.children:
        child_total = 0
        class_count = dna_count_class(child.dna_data)
        r_count.append(class_count[0])
        r_count.append(class_count[1])
        r_count.append(class_count[2])
        child_total = sum(class_count)
        e_count.append(p_values[0]*child_total)
        e_count.append(p_values[1]*child_total)
        e_count.append(p_values[2]*child_total)
    return chi_square(e_count, r_count, dof, alpha)


def chi_square(e_count, r_count, dof, alpha):
    """takes the a list of expected counts for IE, EI and N
    (can be fractions) and the real counts"""
    x2 = chi_sq_dist(dof, alpha)
    xc2 = 0
    for i in range(0, dof+1):
        if e_count[i] != 0:
            xc2 += ((r_count[i] - e_count[i])**2) / e_count[i]
        # also tried not adding r_count submission score was unchanged
        else:
            xc2 += r_count[i]

    # reject null hypothesis
    return not xc2 > x2


def chi_sq_dist(dof, alpha):
    dof2 = [
        {'alpha': 0.20, 'crit_val': 3.219},
        {'alpha': 0.10, 'crit_val': 4.605},
        {'alpha': 0.05, 'crit_val': 5.991},
        {'alpha': 0.025, 'crit_val': 7.378},
        {'alpha': 0.02, 'crit_val': 7.824},
        {'alpha': 0.01, 'crit_val': 9.210},
        {'alpha': 0.005, 'crit_val': 10.597},
        {'alpha': 0.002, 'crit_val': 12.429},
        {'alpha': 0.001, 'crit_val': 13.816}
    ]
    dof3 = [
        {'alpha': 0.20, 'crit_val': 4.642},
        {'alpha': 0.10, 'crit_val': 6.251},
        {'alpha': 0.05, 'crit_val': 7.815},
        {'alpha': 0.025, 'crit_val': 9.348},
        {'alpha': 0.02, 'crit_val': 9.837},
        {'alpha': 0.01, 'crit_val': 11.345},
        {'alpha': 0.005, 'crit_val': 12.838},
        {'alpha': 0.002, 'crit_val': 14.796},
        {'alpha': 0.001, 'crit_val': 16.266}
    ]
    dof7 = [
        {'alpha': 0.20, 'crit_val': 9.803},
        {'alpha': 0.10, 'crit_val': 12.017},
        {'alpha': 0.05, 'crit_val': 14.067},
        {'alpha': 0.025, 'crit_val': 16.013},
        {'alpha': 0.02, 'crit_val': 16.622},
        {'alpha': 0.01, 'crit_val': 18.475},
        {'alpha': 0.005, 'crit_val': 20.278},
        {'alpha': 0.002, 'crit_val': 22.601},
        {'alpha': 0.001, 'crit_val': 24.322}
    ]

    dofX = []
    if dof == 2:
        dofX = dof2
    elif dof == 3:
        dofX = dof3
    elif dof == 7:
        dofX = dof7
    else:
        print ("Unsupported degree of freedom used!")
        return 0

    for cv in dofX:
        if cv['alpha'] == alpha:
            return cv['crit_val']


class ID3Tree(object):
    root = None

    def __init__(self, dna_data=[], use_gini_index=False, alpha=0):
        self.root = ID3Node(None,
                            dna_data=dna_data,
                            use_gini_index=use_gini_index,
                            alpha=alpha)

        if dna_data:
            self.create_tree()
        return

    def create_tree(self):
        """Creates a new decision tree based on the given data."""
        attrs = list(range(0, len(self.root.dna_data[0]['attrs'])))
        values = ['A', 'G', 'T', 'C']
        #values = ['A', 'G', 'T', 'C', 'D', 'N', 'S', 'R']
        self.root.create_subtree(values, attrs)
        return

    def classify_data(self, data):
        """Find the classification for the given testing data.

        :type data: list
        :param data: Parsed testing data to classify.

        :rtype: list
        :returns: A classification for each data item in the testing data set.
        """
        classification = []
        for item in data:
            idx, attrs = item.values()
            cls = self.root.get_class(attrs)
            classification.append({'id': idx,
                                   'class': cls})
        return classification


class ID3Node(object):
    parent = None
    children = []

    dna_data = []
    value = ''
    attr = 0
    cls = ''

    use_gini_index = False
    alpha = 0

    def __init__(self, parent, dna_data=[], value=0,
                 use_gini_index=False, alpha=0):
        self.parent = parent
        self.children = []

        self.value = value
        self.dna_data = dna_data
        self.use_gini_index = use_gini_index
        self.alpha = alpha
        return

    def is_leaf(self):
        """Tests whether this node is a leaf node or not.

        :rtype: bool
        :returns: True if this is a leaf node, False otherwise
        """
        return not self.children

    def is_root(self):
        """Tests whether this node is the root.

        :rtype: bool
        :returns: True if this is the root node, False otherwise
        """
        return not self.parent

    def add_child(self, dna_data, value):
        """Adds a child ID3Node to this node."""
        self.children.append(ID3Node(self,
                                     dna_data=dna_data,
                                     value=value,
                                     use_gini_index=self.use_gini_index,
                                     alpha=self.alpha))
        return

    def get_class(self, attrs):
        """Gets the class for the given set of attrs.

        This function will parse the decision tree to find
        the class for the given set of attributes.

        :type attrs: string
        :param attrs: Attributes to clasify given from testing data.

        :rtype: string
        :returns: The classification for the given attrs,
                  or None if there is not one
        """
        if self.is_leaf():
            return self.cls
        else:
            for child in self.children:
                if child.value == attrs[self.attr]:
                    return child.get_class(attrs)
        return self.cls

    def create_subtree(self, values, attrs):
        # Check is all of the data is the same class, if it is,
        # then this is a leaf node with that class.
        if not self.dna_data:
            self.cls = get_class(self.parent.dna_data)
            return
        else:
            self.cls = get_class(self.dna_data)

        # If no attrs are left to test,
        # then pick the class that occurs the most
        if not attrs or is_same_class(self.dna_data):
            return

        # calculate the gain for each attr
        gain = []
        for attr in attrs:
            if self.use_gini_index:
                gain.append(gini_gain(self.dna_data, values, attr))
            else:
                gain.append(info_gain(self.dna_data, values, attr))

        # gets the attr with the largest gain value,
        # which is the attr we are going to split the tree at
        split_attr = gain.index(max(gain))
        self.attr = attrs[split_attr]
        attrs.remove(self.attr)

        # create children the get a subset of the data
        # based on the value of the data at the split attr
        for value in values:
            split_data = get_subset2(self.dna_data, value, self.attr)
            self.add_child(split_data, value)

        dof = len(values) - 1
        if rej_null_hyp(self, dof, self.alpha):
            # prunechildren and classify node
            self.children = []
            return

        # Recursively create subtrees
        for child in self.children:
            child.create_subtree(values, attrs)
        return
