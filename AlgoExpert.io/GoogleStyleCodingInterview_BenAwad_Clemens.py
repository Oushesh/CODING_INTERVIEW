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

'''
1. Go to the lowest element of the tree. --> one where the other one
has no children and the depth is the least. We have the graph structure -->

2. head = current: define left, right, left_subtree, right_subtree
 #We continue to loop until we reach the top.
 #How do we implement this? --> until query does not given an empty element
 while query(head):
    Get parent(head) --> 3
    Get left, right = chilren(head) --> 7,6  as new left and right
    Initialise left_subtree and right_subtree as [], []
    left_subtree.append(left)
    # Condition to avoid double appending --> assume no double key and there cannot be any double key.
    # No doule key: since we are speaking about a dictionary here. There cannot be any double key.
    Each key is unique.

    right_subtree.append(right)
    head = get_head(left) --> now at 7

That should be it!
'''
def get_last_element(tree):
    '''
    last element is the key which does not have any value
    '''
    for key,value in tree.items():
        if not value:
            return key
        return None

def reverse_tree(tree):
    reverse_tree = {}
    for key,value in tree.items():
        '''
        Key:single element
        value: list of 2 elements: left node, right node
        '''
        key,value = value,key
        reverse_tree[key] = value

    return reverse_tree

def get_parent(child,reverse_tree):
    '''
    given children find the corresponding parents
    Key: list, value: single element
    '''
    for key,value in reverse_tree.items():
        if child in key:
            return reverse_tree[key] #The value is the parents of the input child node
    return None

def get_children(node,tree):
    '''
    children node given the parents
    '''
    return tree[node]

def swap(left,right):
    left,right = right,left
    return left,right

def full_reverse(tree):
    reversed = reverse_tree(tree)
    head, left,right = None
    left_sub, right_sub = []
    if tree:
        last_element = get_last_element(tree)
        if parent:
            #We recursively loop until we have no parent on top of current node
            while get_parent(parent,reversed):
                if last_element:
                    parent=last_element
                    last_element=None
                else:
                    parent = get_parent(parent)
                    left,right = get_children(parent) #get right and left
                    left_sub.append(left)
                    right_sub.append(right)
                    left_sub,right_sub = swap(left_sub,right_sub)
                    left, right = swap(left,right)
                    '''
                    update it in the tree here. left,right swap
                    '''
                    [left, right] = tree[parent]
    return tree

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

    print ('The full reverse binary tree is:',full_reverse(tree_graph))


#TODO: Debugging the unhashable list type
