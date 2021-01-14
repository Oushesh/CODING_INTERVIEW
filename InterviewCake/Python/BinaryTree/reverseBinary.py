'''
Inspired by the interview from Ben Awad with Clemens Mihalescu
on youtube. Reverse Binary Tree.
'''

class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inverseBinaryTee(tree):
    if tree:
        left = tree.left
        right = tree.right
        tree.left = right
        tree.right = left
        #Recurive call
        inverseBinaryTree(tree.left)
        inverseBinaryTree(tree.right)
        return None

#main function to call the Tree here or we can also do in place
if __name__ == "__main__":
    Tree(50)
    Tree.left(30)
    Tree.right(80)
    Tree.left.left(20)
    Tree.left.right(40)
    Tree.left.left.left(10)

    Tree.right.left(70)
    Tree.right.right(90)
    Tree.right.left.left(60)

    Tree.right.right.left(85)
    Tree.right.right.right(100)
    print ('The reversed binary Tree is thus ',inverseBinaryTree(Tree))
