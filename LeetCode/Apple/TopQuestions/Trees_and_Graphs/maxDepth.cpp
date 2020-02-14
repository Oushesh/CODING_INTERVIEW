//how to define a tree in Cpp
#include <iostream>
#include <map>
#include <vector>

using namespace std;
struct TreeNode{
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode (int x):val(x),left(NULL),right(Null){}
};

class Solution{
public:
  int maxDepth(TreeNode * root)
  {
    if (root == NULL)
    {
      return 0;
    }
    else
    {
      int left_height = maxDepth(root->left);
      int right_height = maxDepth(root->right);
      return max(left_height,right_height)+1;
    }
  }
};

int main()
{
  TreeNode node *new node = {3,9,20,NULL,NULL,15,7};
  Solution output;
  cout << "The max depth is:" << output.maxDepth(node)<< endl;
  return 0;
}
