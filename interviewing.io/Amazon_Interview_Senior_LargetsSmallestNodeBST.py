#Reference: https://interviewing.io/recordings/Python-Amazon-2/

'''
This interview is for an SDE 2 role. Senior position
Good one to try.
'''

'''
Grokking a Systems Design Interview
YouTube Channel success in Tech: Success in Tech
System Design Interview
https://github.com/RickSayd/navigating-system-design
'''

'''
Question Definition:
1) Binary Search Trees (BST) have the following
property: Left < Root < Right

2) An in-order traversal would result in visiting
the nodes, in sorted, ascending order (smallest->largest)

#The successor is the next node in the traversal.
# You can assume the node is valid exists somewhere
in the tree.
'''


'''
Example:
     5
   /   \
  3      7
 / \    / \
2   4  6   8

Given a start node, find me the successor_node

5->6 ---> return smallest of right subtree --->

          Logic Derivation:
          node --> get right_node. (7)
          if
          #if node.left < node.right:
            return node.left
7->8 ---> return node.right --> return smallest of right subtree (code up this function)
3->4 --> return smalles of right subtree

2->3 --> add condition: if not node.left or not node.right (Balanced Tree):
         upward traversal.

         #current_node = node.
         #if not node.left or not node.right:
            query (parent)
            if parent == target. then return target




'''
