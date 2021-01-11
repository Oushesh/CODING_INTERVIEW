#This question is focussed on the superbalance
#property of a binary tree.

'''
Reference: https://www.interviewcake.com/question/python3/balanced-binary-tree?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23329:%20Balanced%20Binary%20Tree&utm_medium=email&utm_medium=email&__s=ap5rqqpkspoovezbmxvs

Definition of the problem: A tree is 'superbalanced' if the difference
between the depths of any 2 leaf nodes is no greater than 1.


I go to all the leaf nodes, each time I call the function:
I update the depth by 1

Example, consider the following tree:

        1
      /    \
      2      3
    /  \    / \
    4   5  6   7
  /  \
  8   9


We are going to build the tree iteratively in this case
'''
class Node:
    def __init__(self,node):
        self.left = None
        self.right = None
        self.node = node

#Recursive solution
def max_depth(tree):
    '''
    1. Query on and on until graph does not have children anymore.
       each time add +1
       when you stop that value gives you the depth
    '''
    minDepth = float("Inf")
    maxDepth = 0

    def findDepth(node,depth,minDepth,maxDepth):
        #if the condition is violated we return
        if (maxDepth-minDepth)>1:
            return

        if node.left:
            findDepth(node.left, depth+1, minDepth, maxDepth)
        if node.right:
            findDepth(node.right, depth+1, minDepth, maxDepth)

        #At the leaf node, the current node does not have
        if not node.right and not node.left:
            #go down the tree.
            if depth>maxDepth:
                maxDepth=depth
            if depth<minDepth:
                minDepth=depth

    findDepth(tree,0,minDepth,maxDepth)
    print ('minDepth',minDepth)
    print ('maxDepth',maxDepth)
    return maxDepth - minDepth <=1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)


    #Call the function here:
    print ('The tree is superbalance:',max_depth(root))
