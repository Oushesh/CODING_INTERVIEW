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

class TreeNode
{
  
}
