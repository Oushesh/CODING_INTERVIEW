//Rewriting the code in .cpp
//Rewriting the code: of Superbalanced.py, Superbalanced.cpp

#include <iostream>
#include <vector>
#include <limits>

using namespace std;

struct Node
{
public:
  int value;
  Node* left;
  Node* right;

  Node(int value)
  {
    this->value = value;
    left = NULL;
    right = NULL;
  }
};


/*
Node* buildNode(int value)
{
  Node* node = new Node();
  node->value = value;
  node->left = NULL;
  node->right = NULL;
};
*/

bool max_Depth(Node* node)
{
  //Query on and on until graph does not have any children.
  //each time add +1 Recursive call
  //when you stop that value gives you the depth
  double minDepth = numeric_limits<double>::max();
  double maxDepth = 0;

  void findMinMaxDepth(Node* tree, int depth,double maxDepth, double minDepth)
  {
    if (maxDepth-minDepth >1)
    {
      return;
    }
    if (node->left)
    {
      findMinMaxDepth(node->left,depth+1);
    }
    if (node->right)
    {
      findMinMaxDepth(node->right,depth+1);
    }
    if (!node->left && !node->right)
    {
      if (depth>maxDepth)
      {
        madDepth = depth;
      }
      if (depth<minDepth)
      {
        minDepth=depth;
      }
    }
  }
  findMinMaxDepth(&tree,0);
  cout << "Max Depth:" << maxDepth << endl;
  cout << "Min Depth:" << minDepth << endl;
  return (maxDepth-minDepth) ? true:false;
};

int main()
{
  struct Node* root = new Node(1);
  root->left = new Node(2);
  root->right = new Node(3);
  root->left->left = new Node(4);
  root->left->right = new Node(5);
  root->right->left = new Node(6);
  root->right->right = new Node(7);
  root->left->left->left = new Node(8);
  root->left->left->right = new Node(9);
  cout <<"The tree is superbalanced:" <<max_depth(root)<<endl;
  return 0;
}
