a = [(1, 1), (2, 1), (3, 1), (4, 3), (5, 3), (6, 3), (7, 7), (8, 7), (9, 7)]
# pass 1: create nodes dictionary
nodes = {}
for i in a:
    id, parent_id = i
    nodes[id] = { 'id': id }

# pass 2: create trees and parent-child relations
forest = []
for i in a:
    id, parent_id = i
    node = nodes[id]

    # either make the node a new tree or link it to its parent
    if id == parent_id:
        # start a new tree in the forest
        forest.append(node)
    else:
        # add new_node as child to parent
        parent = nodes[parent_id]
        if not 'children' in parent:
            # ensure parent has a 'children' field
            parent['children'] = []
        children = parent['children']
        children.append(node)

print (forest)
'''
     1
    / \
   2   3
      /  \ \
     4    5 6
 7
/ \
9  8
'''

'''
Consider the next problem:
[1,2,3], [3,4,5], [7,8,9]
Transform to edges
Lets say we have the following datastructure:
[(1,2,3),(3,4,5),(7,8,9)]
Lets build the edges.
'''

class Solution_Trees:
    def build_tree(self,routes):
        nodes  = {}
        #First phase build the the dictionary for nodes phase
        for route in routes:
            parent_id,left,right = route
            nodes[parent_id]     = {'parent_id',(left,right)}
        return nodes

        forest = [] #which will contain all the trees
        for route in routes:
            parent_id,left,right = route
            #start a new tree in the forest
            node = nodes[parent_id]
            print ('node',node)
            if parent_id == node: #either left child or right child
                forest.append(node)
            else:
                parent = nodes[parent_id]
                if not 'children' in parent:
                    parent['children'] = []
                children = parent['children']
                children.append(node)
        return forest



if __name__ == '__main__':
    routes = [(1,(2,3)),(3,(4,5)),(7,(8,9))]
    myRoute = Solution_Trees()
    print ('MyRoute is:', myRoute.build_tree(routes))
