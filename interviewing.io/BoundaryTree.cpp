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



Take care of right-left, left->right ??? How???

traverseL(Node)
 return (Node->left)
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
    BinaryTree->value = value;
    BinaryTree->left = NULL;
    BinaryTree->right = NULL;
  }
};




int main()
{
  //Instantiate the BinaryTree here
  return 0;
}
