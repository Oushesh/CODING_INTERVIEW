//
// Created by Oushesh on 06/07/2020.
//

/*
 Reference:  https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/?ref=rp
 Algorithm:
 1. Take in tree as struct Node with attributes: left,right,value
 2. max of leftsubtree, max of rightsubtree as long as the left or right subtree exists.
 3. go in the direction of the max.
*/



#include "iostream"
using namespace std;

//Node tree type
struct Node
{
    int data;
    struct Node *left, *right;
};

int maxDepth(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    //base case: 1 parent node; no left or right subnode.
    if (root->left == NULL && root->right == NULL)
    {
        return 1;
    }
    //if the left subtree does not exist: recursively
    if (!root->left)
    {
        return maxDepth(root->right)+1;
    }
    if (!root->right)
    {
        return maxDepth(root->left)+1;
    }
    return max(maxDepth(root->left),maxDepth(root->right))+1;
};

Node *newNode(int data)
{
    Node *temp = new Node;
    temp->data = data;
    temp->left = temp->right = NULL;
    return (temp);
}
int main()
{
    Node *root = newNode(1);
    root->left = 2;
    root->right = 3;
    root->left->left = 4;
    root->left->right = 5;
    cout << "The maximum depth of binary tree:" << maxDepth(root);
    return 0;
}
