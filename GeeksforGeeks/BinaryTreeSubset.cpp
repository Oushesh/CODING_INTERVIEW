/*
Given 2 binary Trees, check if the first tree is a subtree of the second one.
A subtree of a tree T is a tree S consisting of a node and all
of its descendsnts in T. The subtree corresponding to the root
node is the entire tree; the subtree corrsponding to any other node
is called a proper subtree.


Example: tree S is a subtree of tree T.


Tree S:


      10
    /    \
   4      6
  /
30




Tree t:

        26
      /   \
     10    3
    /  \    \
   4   6     3
  /
30
*/

/*
We can actually do a trick with PYTHON:
1) We write Tree S and Tree T in set data structure
2) Then we perform set().interection() to get the
*/

/*
In this case we do recursive win:

1. if Tree S or Tree T does not exist: return False or break
2. recursively call root->left and root-right and check if they match, check_identicl.
3. Call this in a different to check similarity of the 2 subtrees.
*/
#include <iostream>
#include <vector>

using namespace std;

//You can also use struct here. Does not matter.
class TreeNode
{
public:
  int value;
  TreeNode* left;
  TreeNode* right;

  //Constructor definition below
  TreeNode(int value)
  {
    this->value = value;
    //initially assign the left and right values to NULL
    this->left = NULL;
    this->right = NULL;
  }
};

//This function returns if the 2 trees are similar.
//iteratively going through root->left and root->right
bool checkIdentical(TreeNode* S, TreeNode* T)
{
  //Edge Cases
  //if both are null, then true.
  //if one is null the other not, then they are not the same.
  //so not.
  if (S==NULL && T==NULL)
    return true;

  if (S==NULL || T==NULL)
    return false;

  //recursive call with TreeNode->left && TreeNode->right
  //continue returning true as long as left of S and T as well right of S and T
  return S->value==T->value && checkIdentical(S->left,T->left) && checkIdentical(S->right,T->right);
}

bool checkSubtree(TreeNode* S, TreeNode* T)
{
  if (S==NULL)
    return false;
  if (T==NULL)
    return false;

  if (checkIdentical(S,T))
    return true;

  //else I pass either the root as root->left or root->right against
  //the T full subtree to tested by checkIdentical in the next function iteration
  return checkSubtree(S-> left,T) || checkSubtree(S->right,T);
}

int main()
{
  TreeNode* S = new TreeNode(26);
  S->left = new TreeNode(10);
  S->right = new TreeNode(3);
  S->left->left = new TreeNode(4);
  S->left->right = new TreeNode(6);
  S->right->right = new TreeNode(3);
  S->left->left->left = new TreeNode(30);

  TreeNode* T = new TreeNode(10);
  T->left = new TreeNode(4);
  T->right = new TreeNode(6);
  T->left->left = new TreeNode(30);

  cout  <<  "T is a subtree?" << checkSubtree(S,T) << endl;
  cout << "ABCD" << endl;
  return 0;
}
