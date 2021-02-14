'''
MaxPathSumBinaryTree

Input:
     1
   /    \
  2      3
 / \    /  \
4   5  6    7

Output: 18 (7-3-1-2-5)

Lets try to write down the thought patterns:
 Here the answer is 7-3-1-2-5.
Define a unique way to do this:

1->left2,3
left_sub.append[1,2], sum=3
right_sub.append[1,3], sum= 4

all possible path: sum them all.
1-2-4 --> 7
1-2-5 --> 8
1-3-6 --> 10
1-3-7 --> 11


1-3 --left_sub ()
1-2 --right_sub

ans = max(root->val+ls+right)

Complexity itself: Branching Factor is 2, depth of tree: d 2^(d-1)
                   Complexity of this solution.
                   Space: O(1) only saving variables.

This is correct.
The output has to be a combination of one or more of the possible paths.
Lets do first in place. Then we build predefined.
'''
class BinaryTree:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None

    def sum(self,root):
        ans = float('-inf')
        if root==None:
            return 0
        left_sub = max(0,self.sum(root.left))
        right_sub = max(0,self.sum(root.right))
        ans = max(ans,root.val+left_sub+right_sub)
        print (ans)
        return root.val+max(left_sub,right_sub)

    def maxPathSum(self,tree):

        output = self.sum(tree)
        return output

if __name__ == "__main__":
    #tree = {1:[2,3],2:[4,5],3:[6,7]}
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print ('The max Path Sum for the given BinaryTree is:',root.maxPathSum(root))


#TODEBUG: check the output vs print
