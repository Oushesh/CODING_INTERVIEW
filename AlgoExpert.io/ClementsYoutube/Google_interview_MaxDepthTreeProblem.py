'''
Reference: https://www.youtube.com/watch?v=-tNMxwWSN_M&t=631s
Binary Tree problem
Title Acing Google Coding Interview as an 18 year old High School Student.
'''

'''
Prompt:
        1
      /    \
      2      3
    /  \    / \
    4   5  6   7
  /  \
  8   9


 Depth of node: Depth here is 3.
 First: Write me a code that takes in the Binary Tree and count the number of node.
 How do you represent the tree? --> Let's say as a tree as a list of nodes.
 each one has a property left_child, right_child

 Go deeper and deeper until you have no children
'''

'''
Focus on the algorithm.
'''

class Node:
    def __init__(self,node):
        self.left = None
        self.right = None
        self.node = node

    def max_depth(self,node):
        '''
        1. Query on and on until graph does not have children anymore.
           each time add +1
           when you stop that value gives you the depth
        '''
        if node is None:
            '''
            Tree does not exist
            '''
            return 0
        else:
            left_depth  = self.max_depth(node.left)
            right_depth = self.max_depth(node.right)

            if (left_depth > right_depth):
                return left_depth+1
            else:
                return right_depth+1

if __name__ == "__main__":
    '''
    Initialise the tree
    '''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)



    ###Different tree here:

    print ('The max depth is:%d'%(root.max_depth(root)))
