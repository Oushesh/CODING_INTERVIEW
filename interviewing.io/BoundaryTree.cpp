/*
Reference: https://stackoverflow.com/questions/30275735/to-print-the-boundary-of-binary-tree

To print the boundary of Binary Tree,
Consider the following:

               1
            /     \
           2      3
          / \    / \
        4    5  6   7
           /    \    \
          8     9     10

Answer is like: 1,2,4,8,9,10,7,3

how do we do this?
1. Classical Definition of BinaryTree,
2. 1,2--> Travel left->left recursively,
    4, 8,9,10 --> Travel and print leaf nodes

Algorithm Thinking and Pseudocode:

Traverse from top to bottom.
Function
traverse(BinaryTree* Node)
  cout << node->val << endl;
  if node->left
   traverseL(NOde->left)


   if node->right
   traverseR(Node-right)
  if node->rightt
    traverse(Node->right)

Take care of right-left, left->right ??? How??? -->

traverseL(Node)
if left
  return (Node->left)
if right
  return traverseC(root->right)

left-right
right-> left
traverseC(Node)
  if (!root->left && !root-right)
    cout << root->vluae << endl; This is the point where we reached the leaf node.
  else
    traverseL(root->left)
    traverseR(root->right)


#Rewrite this in python: again
*/
#include <iostream>
using namespace std;

class BinaryTree
{
public:
  int value;
  BinaryTree* left;
  BinaryTree* right;

  //Build a function to build the tree
  BinaryTree(int value)
  {
    this->value = value;
    this->left = NULL;
    this->right = NULL;
  }
};

void traverseC(BinaryTree* root)
{
  if (!root->left && !root->right) //bottom reached
    cout << root->value << " ";
  else
  {
    if (root->left) traverseC(root->left);
    if (root->right) traverseC(root->right);
  }
}
void traverseL(BinaryTree* root)
{
  cout << root->value << " ";
  if (root->left)
    traverseL(root->left); //still in outer left
  if (root->right)
    traverseC(root->right);
}

void traverseR(BinaryTree* root)
{
  if (root->left)
    traverseC(root->left);
  if (root->right)
    traverseR(root->right); //still in outer right
  cout << root->value<< " ";
}

void traverse(BinaryTree* root)
{
  if (!root)
    return;
  cout << root->value << " ";
  if (root->left)
    traverseL(root->left); //special function for outer left
  if (root->right)
    traverseR(root->right); //special function for outer right
}

int main()
{
  //Instantiate the BinaryTree here
  /*
      1
    /     \
    2      3
    / \    / \
    4  5  6   7
       \   \   \
       8   9   10
  */

  BinaryTree* root = new BinaryTree(1);
  root->left = new BinaryTree(2);
  root->right = new BinaryTree(3);
  root->left->left = new BinaryTree(4);
  root->left->right = new BinaryTree(5);
  root->right->left = new BinaryTree(6);
  root->right->right = new BinaryTree(7);
  root->left->right->left = new BinaryTree(8);
  root->right->left->left = new BinaryTree(9);
  root->right->right->left = new BinaryTree(10);

  traverse(root);
  return 0;
}
