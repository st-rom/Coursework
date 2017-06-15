# A class implementing a node.

class Node:

    def __init__(self, item, next = None):
        """
        Produces a newly constructed empty node.
        __init__: Any -> Node
        Fields: item stores any value
            next points to the next node in the list
        """
        self.item = item
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        for i in self.item:
            return str(i)

    def __len__(self):
        '''
        Returns length of the dictionary's value
        __len__: Node -> Int
        '''
        for i in self.item:
            return len(self.item[i])
