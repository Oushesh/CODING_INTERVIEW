'''
Reference: https://www.geeksforgeeks.org/iterative-approach-to-check-if-a-binary-tree-is-bst-or-not/?ref=rp
'''

'''
Iterative Approach to check if a Binary Tree is BST or not.
'''
'''
Input: Binary Tree
Output : Boolean: True or False

Example:
            9
          /   \
         6    10
       /   \    \
      4     7    11
    /   \    \
    3    5    8

10>9>6, 11>10, 7>6>4, 5>4>3, 8>7 True.
How did we do this? node.right > node.root > node.left
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



def checkBST(root:Node):
    stack = []
    prev = None

    #Traverse down the tree.

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if prev and root.value <= prev.value:
            return False

        prev=root

        root = root.right
    return True



if __name__ == "__main__":
    #Initialise the Binary Tree here:
    root = Node(9)
    root.left = Node(6)
    root.right = Node(10)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.right.right = Node(11)
    root.left.left.left = Node(3)
    root.left.left.right = Node(5)
    root.left.right.right = Node(8)


    print ('The given tree is BST:',checkBST(root))
