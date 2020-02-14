
#Delete node.

#Find mistake in reverse array.
#Easy stuffs, temporary swap algorithm
#
'''
Task 1:
Find mistake in reverse array.
Correct the code
Easy stuffs, temporary swap algorithm
'''

'''
Task 2:
Leetcode:
Given a 2D gird map of 1's (land) and O's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all 4 edges of the grid are all surrounded by
water.
TODO
'''

'''
We want to delete certain nodes from a binary tree. We have a function
'shouldDelete(TreeNode node)' that returns true if we should delete that
node, you can assume this function already exists.

Write a function 'deleteNodes(TreeNode root)' that takes a binary tree
which removes the nodes that should be deleted from the tree and returns
a forest of trees.
'''

'''
Binary Tree:
How to represent the tree?
{A:0}->{B:0}->{C:0}
{B:0}->{D:0}->{E:0}
{C:0}->{F:0}->{G:0}

Lets define the tree as a list of lists
'''

'''
Let's say each node is instead a dictionary, then the node is the key
and the value is the boolean (True, False) telling me whether I should delete
the node or not.
'''

'''

'''

class TreeNode:
    def __init__ (self,tree):
        self.left =  None
        self.right = None
        self.value = value

    def PrintTree(self):
        print(self.value)

    def insert(self,existingTree,List):
        self.left  = List[1]
        self.right = List[2]
        self.parent = List[0]
        #Perform check on existing tree
        if 



if __name__ == '__main__':
    tree = [1,2,3]
    root.insert([1,2,3])
    root.insert([3,4,5])

    #Call the insert method here:
