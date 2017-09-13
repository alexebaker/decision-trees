from __future__ import print_function
from __future__ import unicode_literals


class ID3Tree(object):
    root = None

    def __init__(self, data=None):
        self.root = ID3Node(None)

        if data:
            self.create_tree(data)
        return

    def create_tree(self, data):
        """Creates a new decision tree based on the given data.

        :type data: list
        :param data: Parsed data from the training data set.
        """
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

    cls = 'N' # Setting to N for testing purposes

    def __init__(self, parent):
        self.parent = parent
        self.children = []
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

    def add_child(self):
        """Adds a child ID3Node to this node."""
        self.children.append(ID3Node(self))
        return

    def get_class(self, attrs):
        """Gets the class for the given set of attrs.

        This function will parse the decision tree to find
        the class for the given set of attributes.

        :type attrs: string
        :param attrs: Attributes to clasify given from testing data.

        :rtype: string
        :returns: The classification for the given attrs, or None if there is not one
        """
        if self.is_leaf():
            return self.cls
        else:
            for child in self.children:
                cls = child.get_class(attrs)
                if cls:
                    return cls
        return None
