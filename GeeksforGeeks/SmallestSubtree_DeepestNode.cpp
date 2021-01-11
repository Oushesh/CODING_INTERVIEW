/*
Given a Binary Tree, the task is to find the
smallest sutree that contains all the deepest nodes.

Input:
           1
         /    \
        2      3
      /  \    / \
     4   5   6   7
                / \
              8    9

OUtput: 7 --> Smallest subtree is: thus:
                                        7
                                      /  \
                                    8     9

Strategy is really simple:

DFS -> recursive approach. O(V+E), O(n): n depth of leaf node.
                           if the Tree were balanced: BST (Ologn)

1. if depth of left subtree > right subtree --> Traverse left subtree --> update depth+1
2. elif depth of right subtree > left subtree --> Traverse leftsubree --> update depth+1
3. if left.node or right.node does not have children --> return that node.
*/

#include <iostream>
#include <vector>

using namespace std;

struct TreeNode
{
  TreeNode* left;
  TreeNode* right;
  int val;

  //Something to build the tree

  TreeNode(int val)
  {
    //you use the famous this.
    this->val = val;
    left = NULL;
    right = NULL;
  }
};

//Function to return depth of the Tree from root
//we iterate we go to that depth
int find_depth(TreeNode* root)
{
  if (!root)
    return 0;

  if (root->left == NULL && root->right == NULL)
    return 1;

  return max(find_depth(root->left),find_depth(root->right))+1;
}


//We have to return the
TreeNode* find_node(TreeNode* root)
{
  TreeNode* requested_node;
  //Handle the case where
  if (!root)
  {
    requested_node = NULL;
    return requested_node;
  }

  int right_depth = find_depth(root->right);
  int left_depth  = find_depth(root->left);

  //We go in the direction of the highest node.
  if (left_depth>right_depth)
    //Traverse left_subtree
    find_node(root->left);
  else if (right_depth>left_depth)
    find_node(root->right);
  //in the else part we have both the same we reached the leaf node
  else
  {
    requested_node = root;
    return requested_node;
  }
}

int main()
{
  struct TreeNode* root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->left = new TreeNode(6);
  root->right->right = new TreeNode(7);
  root->right->right->left = new TreeNode(8);
  root->right->right->right = new TreeNode(9);

  TreeNode* output_node;
  output_node = find_node(root);

  cout << output_node->val << endl;
  return 0;
}
