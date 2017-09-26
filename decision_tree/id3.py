from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import math


def gini_value(dna_data):
    """Calculates the gini value for a set of dna data.

    This calculates the gini value by taking the probabilty of each classification and multiplies them together.

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :rtype: float
    :returns: Calculated gini_value based on the dna data.
    """
    p_values = dna_p_value(dna_data)
    gini_value = 1
    if not p_values:
        return 0
    else:
        for p in p_values:
            gini_value *= p
    return gini_value


def gini_gain(dna_data, values, attr):
    """Calculates the gain for a set of dna data based on the gini value.

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :type values: list
    :param values: List of values to calculate the gain accross

    :type attr: int
    :param attr: Attribute to calculate the gain for

    :rtype: float
    :returns: Calculated gain based on the gini value.
    """
    gain = gini_value(dna_data)
    for value in values:
        subset = get_subset(dna_data, value, attr)
        if subset:
            gain -= gini_value(subset)
    return gain


def is_same_class(dna_data):
    """Returns the class of the data if all the data shares the same class.

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :rtype: bool
    :returns: True if the dna data is all the same class, False otherwise
    """
    clses = [dna['class'] for dna in dna_data]
    return clses.count(clses[0]) == len(clses)


def get_class(dna_data):
    """Returns the class that occurs most frequently in the given dna data

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :rtype: str
    :returns: The most common dna class in the dna data
    """
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


def get_subset(dna_data, value, attr):
    """Gets a subset of the data where attr has the given value.

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :type values: list
    :param values: List of dna values

    :type attr: int
    :param attr: Attribute in the dna data

    :rtype: float
    :returns: Calculated gain based on the gini value.
    """
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for dna in dna_data:
        if dna['attrs'][attr] == 'A':
            a_count +=1
        elif dna['attrs'][attr] == 'C':
            c_count +=1
        elif dna['attrs'][attr] == 'G':
            g_count +=1
        elif dna['attrs'][attr] == 'T':
            t_count +=1
        else:
            continue

    subset = []
    for dna in dna_data:
        if dna['attrs'][attr] == value:
            # If the value of the attribute is what we are testing, add this dna to the subset
            subset.append(dna)
        elif dna['attrs'][attr] == 'D':
            if (value == 'A')and(a_count>=g_count)and(a_count>=t_count):
                # value is A and A is most probable
                subset.append(dna)
            elif (value == 'G')and(g_count>a_count)and(g_count>t_count):
                # value is G and G is most probable
                subset.append(dna)
            elif (value == 'T')and(t_count>a_count)and(t_count>g_count):
                # value is T and T is most probable
                subset.append(dna)
        elif dna['attrs'][attr] == 'N':
            if (value == 'A')and(a_count>=c_count)and(a_count>=g_count)and(a_count>=t_count):
                # value is A and A is most probable
                subset.append(dna)
            elif (value == 'C')and(c_count>a_count)and(c_count>g_count)and(c_count>t_count):
                # value is C and C is most probable
                subset.append(dna)
            elif (value == 'G')and(g_count>c_count)and(g_count>a_count)and(g_count>t_count):
                # value is G and G is most probable
                subset.append(dna)
            elif (value == 'T')and(t_count>c_count)and(t_count>a_count)and(t_count>g_count):
                # value is T and T is most probable
                subset.append(dna)
        elif dna['attrs'][attr] == 'S':
            if (value == 'C')and(c_count>=g_count):
                # value is C and C is most probable
                subset.append(dna)
            elif (value == 'G')and(g_count>c_count):
                # value is G and G is most probable
                subset.append(dna)
        elif dna['attrs'][attr] == 'R':
            if (value == 'A')and(a_count>=g_count):
                # value is A and A is most probable
                subset.append(dna)
            elif (value == 'G')and(g_count>a_count):
                # value is G and G is most probable
                subset.append(dna)
    """for dna in dna_data:
        if dna['attrs'][attr] == value:
            # If the value of the attribute is what we are testing, add this dna to the subset
            subset.append(dna)
        elif dna['attrs'][attr] == 'D':
            if any([value == 'A', value == 'G', value == 'T']):
                # D can take on A, G, T values, so add this dna to these subsets
                subset.append(dna)
        elif dna['attrs'][attr] == 'N':
            # N can take on any value, so add this dna to all subsets
            subset.append(dna)
        elif dna['attrs'][attr] == 'S':
            if any([value == 'C', value == 'G']):
                # S can take on C and G values, so add this dna to these subsets
                subset.append(dna)
        elif dna['attrs'][attr] == 'R':
            if any([value == 'A', value == 'G']):
                # R can take on A and G values, so add this dna to these subsets
                subset.append(dna)"""
    return subset


def info_gain(dna_data, values, attr):
    """Calculates the information gain for the given parameters.

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :type values: list
    :param values: List of values to calculate the gain accross

    :type attr: int
    :param attr: Attribute to calculate the gain for

    :rtype: float
    :returns: The calculated information gain for the given parameters.
    """
    sum_total = 0
    for value in values:
        subset = get_subset(dna_data, value, attr)
        if subset:
            sum_total += (len(subset) / len(dna_data)) * entropy(subset)

    return entropy(dna_data) - sum_total


def dna_p_value(dna_data):
    """Calculates probabilty of each of the 3 classes for a set of strands.

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :rtype: tuple
    :returns: A tuple of the probability for (EI, IE, N)
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

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :rtype: tuple
    :returns: A tuple of the counts for (EI, IE, N)
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
    """Calculates the entropy for a set of dna data

    :type dna_data: dict
    :param dna_data: Set of parsed dna data.

    :rtype: float
    :returns: The calculated entropy for a set of dna data
    """
    p_values = dna_p_value(dna_data)

    total = 0
    for p in p_values:
        if p != 0:
            total -= p * math.log(p, 2)
    return total


def rej_null_hyp(pNode, dof, alpha):
    """Calculates the counts needed to use chi_square.

    :type pNode: ID3Node
    :param pNode: Node to calculate chi squared for

    :type dof: int
    :param dof: Degrees of freedom of the data

    :type alpha: float
    :param alpha: alpha value to use in the lookup table

    :rtype: bool
    :returns: Whether or not to split at the given branch
    """
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
    (can be fractions) and the real counts.

    :type e_count: int
    :param e_count: e_count value

    :type r_count: int
    :param r_count: r_count value

    :type dof: int
    :param dof: Degrees of freedom of the data

    :type alpha: float
    :param alpha: alpha value to use in the lookup table

    :rtype: bool
    :returns: The result of the chi squared test
    """
    x2 = chi_sq_dist(dof, alpha)
    xc2 = 0
    for i in range(12):
        if e_count[i] != 0:
            xc2 += ((r_count[i] - e_count[i])**2) / e_count[i]
        # also tried not adding r_count submission score was unchanged
        else:
            xc2 += r_count[i]

    # reject null hypothesis
    return not xc2 > x2


def chi_sq_dist(dof, alpha):
    """Calculates the critical value for chi squared.


    :type dof: int
    :param dof: Degrees of freedom of the data

    :type alpha: float
    :param alpha: alpha value to use in the lookup table

    :rtype: float
    :returns: The critical value based on the lookup table
    """
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
    dof6 = [
        {'alpha': 0.20, 'crit_val': 8.558},
        {'alpha': 0.10, 'crit_val': 10.645},
        {'alpha': 0.05, 'crit_val': 12.592},
        {'alpha': 0.025, 'crit_val': 14.449},
        {'alpha': 0.02, 'crit_val': 15.033},
        {'alpha': 0.01, 'crit_val': 16.812},
        {'alpha': 0.005, 'crit_val': 18.548},
        {'alpha': 0.002, 'crit_val': 20.791},
        {'alpha': 0.001, 'crit_val': 22.458}
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

    dof11 = [
        {'alpha': 0.20, 'crit_val': 14.631},
        {'alpha': 0.10, 'crit_val': 17.275},
        {'alpha': 0.05, 'crit_val': 19.675},
        {'alpha': 0.025, 'crit_val': 21.920},
        {'alpha': 0.02, 'crit_val': 22.618},
        {'alpha': 0.01, 'crit_val': 24.725},
        {'alpha': 0.005, 'crit_val': 26.757},
        {'alpha': 0.002, 'crit_val': 29.354},
        {'alpha': 0.001, 'crit_val': 31.264}
    ]

    dof14 = [
        {'alpha': 0.20, 'crit_val': 18.151},
        {'alpha': 0.10, 'crit_val': 21.064},
        {'alpha': 0.05, 'crit_val': 23.685},
        {'alpha': 0.025, 'crit_val': 26.119},
        {'alpha': 0.02, 'crit_val': 26.873},
        {'alpha': 0.01, 'crit_val': 29.141},
        {'alpha': 0.005, 'crit_val': 31.319},
        {'alpha': 0.002, 'crit_val': 34.091},
        {'alpha': 0.001, 'crit_val': 36.123}
    ]

    dofX = []
    if dof == 2:
        dofX = dof2
    elif dof == 3:
        dofX = dof3
    elif dof == 6:
        dofX = dof6
    elif dof == 7:
        dofX = dof7
    elif dof == 11:
        dofX = dof11
    elif dof == 14:
        dofX = dof14
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
        """Main sub routine that creates the decision tree.

        :type values: list
        :param values: List of values to use for creating the tree

        :type attrs: str
        :param attrs: Attrs to use to create this subtree
        """
        # If no dna data was given to this child, then use the data at the parent node
        if not self.dna_data:
            self.cls = self.parent.cls
            return
        else:
            self.cls = get_class(self.dna_data)

        # If no attrs are left to test, then stop making children
        # Or if the dna has all the same class
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
            split_data = get_subset(self.dna_data, value, self.attr)
            self.add_child(split_data, value)

        #dof = len(values) - 1
        dof=6
        if rej_null_hyp(self, dof, self.alpha):
            # prunechildren
            self.children = []
            return

        # Recursively create subtrees
        for child in self.children:
            child.create_subtree(values, attrs)
        return
