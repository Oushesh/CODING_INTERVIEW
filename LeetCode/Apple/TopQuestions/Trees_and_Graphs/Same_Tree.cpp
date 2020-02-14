#include <iostream>
#include <map>


using namespace std;
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      //TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };

class Solution
{
  bool isSameTree(TreeNode *p, TreeNode *q)
  {
    if ( !p && !q)
    {
      return true;
    }
    if (!p or !q)
    {
      return false;
    }
    if (p->val!=q->val)
    {
      return false;
    }
    return isSameTree(p->left,q->left) && isSameTree(p->left,q->right);
  }
};



int main()
{
  Solution output;
  sturct TreeNode * p = new TreeNode(1) ;
  p ->left = new TreeNode(2);
  p ->right = new TreeNode(1);

  sturct TreeNode * q = new TreeNode(1);
  q->left = new TreeNode(2);
  q->right = new TreeNode(1);

  cout << output.isSameTree(p,q) << endl;
  return 0;
}
