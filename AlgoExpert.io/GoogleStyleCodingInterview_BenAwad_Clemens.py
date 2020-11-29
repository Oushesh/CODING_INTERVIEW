'''
Reference: https://www.youtube.com/watch?v=vHKzIPwWQkg
This coding interview contains 2 questions:

1. Inverse a LinkedList
2. Inverse a Binary Tree.

Directly we know that this involves a recursion algorithmic thinking
strategy.

Set Data Structure: https://www.geeksforgeeks.org/sets-in-python/
'''


#Google Style interviews

'''
Given a pointer to the head node of the linked list,
the task is to reverse it
'''


#a->b->c
#c->b->a
'''
Space Complexity here is: O(1)
we are overwriting every variable

Time: O(n) -> loop over all of them. where n= len(LinkedList)
TODO: reverse LinkedList
'''

class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next  = None

    def reverseLinkedList(self,head):
        new_head = None
        curr = head
        previous = None

        while True:
            #Break if next does not exist
            tmp_curr  = curr.next #store the variable here in temporary memory
            curr.next = previous
            previous  = curr

            if not tmp_curr:
                break
            curr     = tmp_curr
            return curr

'''
Recursive call:
BinaryTree has left and right

        1
      /    \
     2      3
    / \    / \
   4   5  6   7
  / \
 8   9

self.right = self.left
left = right

          1
        /    \
       3      2
      / \    / \
     7   6   5  4
               / \
              9   8
'''
class BinaryTree():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def invertBinaryTree(tree):
    #hi youtube ,) Ben Awad style
    if tree:
        left = tree.left
        right = tree.right
        tree.left = right
        tree.right = left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
        return None

def invertBinaryTree_Graph(tree):
    '''
    input type: tree of type graph
    rtype: graph with key elements reversed
    '''
    if tree:
        for node in tree.keys():
            if tree[node]:
                #reverse the children here
                tree[node].reverse()
    return tree

#Recursive call is DFS
def print_tree(node):
    if (node == None):
        return

    print ('main Value',node.value)
    print_tree(node.left)
    print_tree(node.right)

'''
Input Binary Tree:
    1
  /    \
 2      3
/ \    / \
4   5  6   7
/ \
8   9

Output Binary Tree:
         1
      /     \
     3       2
    / \    /   \
   7   6   5    4
  / \
 8   9
'''

def full_reverse(tree):

    return None

if __name__ == "__main__":
    #list = LinkedList()
    '''
    BinaryTree
    The following representation or
    just use a Graph to represent the tree
    '''
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    #Recursive function to print tree
    #Reinstantiate the object
    print_tree(root)

    print ('inverting...')
    invertBinaryTree(root)
    print_tree(root)

    '''
    Graph representation of tree
    '''
    tree_graph = {1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[],6:[],7:[]}
    print ('Binary Tree', tree_graph)

    #now invert the tree inside flip left to right
    print ('The reverse Binary Tree is:',invertBinaryTree_Graph(tree_graph))
