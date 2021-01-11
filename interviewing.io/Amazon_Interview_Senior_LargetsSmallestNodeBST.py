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
property: Left < Root < Right (Balanced)

2) An in-order traversal would result in visiting
the nodes, in sorted, ascending order (smallest->largest)

#The successor is the next node in the traversal.
# You can assume the node is valid exists somewhere
in the tree.
'''

'''
Example:
      5
   /    \
  3      7
 / \    / \
2   4  6   8

Given 5->6
Given 6->7
Given 8->None

* Assume BST well-formed
Brute Force:

Optimisation:
1) Binary Search Algorithm and try to preprocess it
2) a) 5->6 (smallest--->largest)  (5->7->6, get smallest of right subtree if subtree exists)
   b) 6->7 (smallest--->largest)  ()


The technique is:
--> if right subtree is not None:
    return min(rightsutree)

--> if right subtree does not exist then it is
the ancestor lies in the ancestors of the node.


Travel down the tree, if node.val > root.val --> go right
##################################################################
General Overview of the complexity of search in a balanced tree.
1) O(log(n)) --> depth, d: O(d)
2) O(n), if the tree is unbalanced.
##################################################################

'''
# Python program to find
# the inroder successor in a BST

# A binary tree node
class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def inOrderSuccessor(root, n):

	# Step 1 of the above algorithm
	if n.right is not None:
		return minValue(n.right)

	# Step 2 of the above algorithm
	succ=Node(None)

	while(root):
		if(root.data<n.data):
			root=root.right
		elif(root.data>n.data):
			succ=root
			root=root.left
		else:
			break
	return succ

# Given a non-empty binary search tree,
# return the minimum data value
# found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
	current = node

	# loop down to find the leftmost leaf
	while(current is not None):
		if current.left is None:
			break
		current = current.left

	return current


# Given a binary search tree
# and a number, inserts a
# new node with the given
# number in the correct place
# in the tree. Returns the
# new root pointer which the
# caller should then use
# (the standard trick to avoid
# using reference parameters)
def insert( node, data):
	# 1) If tree is empty
	# then return a new singly node
	if node is None:
		return Node(data)
	else:

		# 2) Otherwise, recur down the tree
		if data <= node.data:
			temp = insert(node.left, data)
			node.left = temp
			temp.parent = node
		else:
			temp = insert(node.right, data)
			node.right = temp
			temp.parent = node

		# return the unchanged node pointer
		return node

# Driver progam to test above function
if __name__ == "__main__":
    root = None
    root = insert(root, 20)
    root = insert(root, 8);
    root = insert(root, 22);
    root = insert(root, 4);
    root = insert(root, 12);
    root = insert(root, 10);
    root = insert(root, 14);
    temp = root.left.right

    succ = inOrderSuccessor( root, temp)
    if succ is not None:
    	print("Inorder Successor of" ,
    			temp.data ,"is" ,succ.data)
    else:
    	print("InInorder Successor doesn't exist")
