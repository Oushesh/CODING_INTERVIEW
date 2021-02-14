/*
MaxPathSumBinaryTree
Reference from here: https://www.youtube.com/watch?v=xUHohVsidLA Clements Mihalescu Coding Interview
Leetcode Reference: https://leetcode.com/problems/binary-tree-maximum-path-sum/


         1
      /    \
     2      3
   /   \   /   \
  4   5   6    7


Max Path Sum is 18: 1+3+7+2+5 = 18

The basics is that we travel from the top:
1.  we travel from the top to the bottom.
2.  max(sum)--> mas of individuals components of the huge sum
3.  left_sub --> recursive call.
4. right_sub --> recursive call.
   max(left_sub,right_sub): sum
   ans  = max(ans,max+left+right)
*/

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;
class TreeNode
{
public:
  int val;
  TreeNode *left;
  TreeNode *right;

  //Lets build a constructor here
  TreeNode(int val)
  {
    this->val = val;
    this->left = NULL;
    this->right = NULL;
  }
};

//Class to get the path sum here.
//max Path Sum
class Path
{
public:
  //we set the answer to the most -ve number to
  //we need a recursive fucntion call here.
  int ans = INT_MIN;
  int sum(TreeNode * root)
  {
    //Edge Case
    if (root==NULL)
      return 0;

    int left_sub = max(0,sum(root->left)); //Just in case the numbers are -ve
    int right_sub = max(0,sum(root->right)); //just in case the numbers aree -ve
    ans = max(ans,root->val+left_sub+right_sub);
    return root->val+max(left_sub,right_sub);
  }
  int maxPathSum(TreeNode *root)
  {
    sum(root);
    return ans;
  }
};

int main()
{
  //initialise the tree here.
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->left = new TreeNode(6);
  root->right->right = new TreeNode(7);

  //Now we perform the algorithm for finding the maximum path sum here.
  Path current_tree;
  cout << "The max Path Sum is:" << current_tree.maxPathSum(root) << endl;
  return 0;
}
