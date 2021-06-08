'''
Ref: https://start.interviewing.io/interview/hz1Mo0I3a8j8/replay
'''


'''
A node is defined as:
int value
Node* left
Node* right

all values unique

What I know is:

right > root > left
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def validate_BST(node):
    if node == None:
        return True
    #Loop until we reach the end of the tree.
    if not node.left == None and node.left.value > node.value:
        return False
    if not node.right == None and node.value>node.right.value:
        return False
    if not validate_BST(node.left) or not validate_BST(node.right):
        return False
    return True

'''
      2 
    1     4 
        3   5
'''

if __name__ == "__main__":
    ##Exmaple Tree:
    graph = Node(2)
    graph.left = Node(1)
    graph.right = Node(4)
    graph.right.left = Node(3)
    graph.right.right = Node(5)
    print (graph.right.value)
    print (validate_BST(graph))





