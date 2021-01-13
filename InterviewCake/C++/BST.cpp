/*
Test BST.cpp
*/


/*
             50
          /     \
        30       80
      /   \     /   \
    20    40   70    90
  /           /     /  \
10          60     85  100


1. Tree balance if left < root < right
*/

#include <iostream>

using namespace std;

class BinaryTree
{
public:
  int value;
  BinaryTree* left;
  BinaryTree* right;

  //Constructor-> input(value)--> build the tree
  BinaryTree(int value)
  {
    this->value = value;
    this->left = NULL;
    this->right = NULL;
  }
};


//This function independently checks the left and right
bool BalanceSubtree(BinaryTree* root)
{
  //Recursive call until I reach the end.
  //Check the left subpart of the tree.
  if (root != NULL)
  {
    if (root->left->value < root->value)
      return BalanceSubtree(root->left);
    else
      return false;
  }
  if (root != NULL)
  {
    if (root->right->value > root->value)
      return BalanceSubtree(root->right);
    else
      return false;
  }
}

bool isBinary(BinaryTree* root)
{
  //Edge Case if the tree does not exist
  if (root == NULL)
    return false;

  if (BalanceSubtree(root))
    return true;
}


int main()
{
  //Build the tree here:
  BinaryTree* root = new BinaryTree(50);
  root->left = new BinaryTree(30);
  root->right = new BinaryTree(80);
  root->left->left = new BinaryTree(20);
  root->left->right = new BinaryTree(40);
  root->left->left->left = new BinaryTree(10);

  root->right->left = new BinaryTree(70);
  root->right->right = new BinaryTree(90);
  root->right->left->left  = new BinaryTree(60);

  root->right->right->left = new BinaryTree(85);
  root->right->right->right = new BinaryTree(100);

  cout << "Is Tree Binary?" << isBinary(root) << endl;
  return 0;
}
