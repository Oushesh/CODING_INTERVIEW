
'''
Given binary tree [3,9,20,null,null,15,7]

  3
   / \
  9  20
    /  \
   15   7
'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

#Depth FIrst search
#Recursion
class Solution:
    def maxDepth(self,root:TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height,right_height)+1

if __name__ == "__main__":
    root = [3,9,20,null,null,15,7]
    print ("The max Depth:",root)
