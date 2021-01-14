'''
The easiest way is to rewrite the tree as a graph structure
in terms of set data structure:
Tree S, Tree t --> rewrite the graph as set structure,
then perform a set intersection function --> if True, then
return True (S is a subset of T)
'''


'''
Consider the 2 following trees:

Tree 1:
               1
            /     \
           2      3
         /  \
        8    9
      /       \
     5         6

Tree 2:
          2
         /  \
        8    9
'''

class Tree:
    def build(self,triplets):
        #Build the tree
        tree = set()
        for tri in triplets:
            tree.add(tri)
        return tree

    def subtree(self,tree1,tree2):
        '''
        Tree1 is the main tree --> bigger tree
        Tree2 is the subtree --> smaller tree
        '''
        if tree1.intersection(tree2):
            return True
        return False

if __name__ == "__main__":
    triplets1 = [(1,2,3),(2,8,9),(8,5),(9,6)]
    triplets2 = [(2,8,9)]

    #Call the function here: build Tree1 & Tree2
    #THen perform the intersection between the 2 sets, set1 and set 2
    current_tree = Tree()
    tree1 = current_tree.build(triplets1)
    tree2 = current_tree.build(triplets2)
    print ('Tree1 ',current_tree.subtree(tree1,tree2))
