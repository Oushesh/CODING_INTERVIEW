/*
Lets reverse the Binary Tree and write and inorder traversal
to print out the results.
*/

/*
             50
          /     \
        30       80
      /   \     /   \
    20    40   70    90
  /           /     /  \
10          60     85  100


How do we reverse the tree?
Basically left_subtree swapped with right_subtree:

Let's do it inplace here -->
temp = root->left
root->left = root->right
root->right = temp

recursively call the function with root->left, root->right


             50
          /     \
        30       80
      /   \     /   \
    20    40   70    90
  /           /     /  \
10          60     85  100

*/
#include <iostream>
using namespace std;

class BinaryTree
{
public:
  int value;
  BinaryTree* left;
  BinaryTree* right;

  //Constructor definition
  BinaryTree(int value)
  {
    this->value = value;
    this->left = NULL;
    this->right = NULL;
  }
};

void reverseTree(BinaryTree* root)
{
  BinaryTree* temp;
  if (root == NULL)
    return;
  else
  {
    //Perform swapping here:
    temp = root->left;
    root->left = root->right;
    root->right = temp;
  }
  if (root->left != NULL)
    reverseTree(root->left);

  if (root->right != NULL)
    reverseTree(root->right);
}

//Traverse the tree and print all the elements
void printTree(BinaryTree * node)
{
  if (node == NULL)
    return;
  cout << node->value <<" ";
  printTree(node->left);
  printTree(node->right);
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

  //Here we do the inorder traversal of the BInarytree to print
  //out the reversed elements
  reverseTree(root);
  printTree(root);

  //Call the function to print here:
  cout << "The reversed BinaryTree is:" << endl;
  return 0;
}
