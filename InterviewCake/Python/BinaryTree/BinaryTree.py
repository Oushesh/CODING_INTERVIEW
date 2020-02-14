#Definition of a BinaryTree
#Find the second largest element in the tree.
#1. Find the largest element in the tree
class BinaryTreeNode(object):
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self,value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self,value):
        self.right = BinaryTreeNode(value)
        return self.right

    #Let's assume the rightmost element is the largest.
    def find_largest(root_node):
        current = root_node
        while current:
            if not current.right:
                return current.value
            current = current.right


    #We can find the largest walk down the tree.
    #With this in mind we can also find the second largest
    #in 1 walk down the tree.

    #1. if we have a right child, but that right chid
    #node does not have any more children.
    #Then right child is largest element.
    #Else, we have right subtree with more than 1 element,
    #so largest and second largest are somewhere in that
    #subtree. So step right.

    def find_second_largest(root_node):
        if (root_node is None or root_node.left is None and root_node.right is None):
            raise ValueError('Tree must have at least 2 nodes')

        current  = root_node
        while current:
            #Case; current is parent or largest, and
            #largest has no children, so current is 2nd largest

            if (current.right and not current.right.left and not current.right.right):
                return current.value

            if current.left and not current.right:
                return find_largest(current.left)
