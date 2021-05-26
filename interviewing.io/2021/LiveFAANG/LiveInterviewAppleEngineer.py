'''
2 questions given:
A) Count duplicates with respect to the constraint:
   Linear Time and Constant space.

B) See the tree from the right side of the problem
'''

'''
Given an array of integers nums containing
n+1 integers where each integer is in the
range [1,n] inclusive.

There is only 1 repeated number in nums,
return this repeated number.

only constant extra space.
'''

'''
Lets say we do not have space constraint.
1. Approach: use a Hash map/python dict.
   Space: O(n)
   Time: O(n)
'''

'''
Now with time and space constraint:
time. O(n) --> 1 loop max.
Space: O(1) --> Cannot save any extra list
'''

def find_duplicate(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num]=1
        else:
            freq[num]+=1
            duplicate = num
    return duplicate

'''
Example: [1,3,4,2,2]
Output: 2

Constraint: constant space
There is no way to solve this without more conditions.
Condition: each number is [1,n]

1,3,4,2,2
1,2,3,4,5 --> Use the indices to find duplicates.

For example:
nums:     1,2,3,4,5
indices:  1,2,3,4,5

as long as number==index:
 mark as visited. mayber with negative -1

 example 2: -1,3,-4,-2,2
             1,2,3, 4, 5
'''


'''
Binary Tree.
Given the root of a binary tee, imagine
yourself standing on the right side of it,
return the values of the nodes you can See
ordered from top to bottom.



  1       <- [1]
 / \
2   3     <- [2, 3]
 \   \
  5   4   <- [5, 4]
  /
 7        <- [7]

[]
Example: Input: root = [1,2,3,null,5,null,4]
         Output: [1,3,4,7]

BFS on the tree or level traversal.
Level 1: [1]
Level 2: [2,3]
Level 3: [5,4]
Level 4: [7]

output = []
level = [], level.append(root.val)
current_level  = []
query_left,query_right
'''


'''
     1
   /     \
   2      3
  /  \   /  \
None  5 None 4

Lets use BFS method for level traversal
and then do output.append([-1]) for the
last element in python
'''

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    # Base Case
    if root is None:
        return []
    queue = []
    queue.append(root)
    level = []
    output = []
    while(len(queue) > 0):
        node = queue.pop(0)
        if node.left is not None:
            output.append(queue[-1])
            queue.append(node.left)
        if node.right is not None:
            output.append(queue[-1])
            queue.append(node.right)
    return output


def rightmost(root):
    if not root:
        return []
    level = []
    output = []
    level.append(root)
    while len(level):
        output.append(level[-1].val)
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    return output


if __name__ == '__main__':
    #Driver Program to test above function
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = None
    root.left.right = Node(5)
    root.right.left = None
    root.right.right = Node(4)
    root.left.right.left = Node(7)
    #print (level_order_traversal(root))
    print (rightmost(root))
