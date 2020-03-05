class Tree:
    def __init__(self, tree, left=None, right=None):
        self.tree = tree
        self.left = left
        self.right = right

    def __str__(self):
        return (str(self.tree) + ', Left' + str(self.left) + ', Right child: ' + str(self.right))

class Tree_List:
    def createTreeFromEdges(self,edges):
        tree = {}
        for v1, v2 in edges:
            tree.setdefault(v1, []).append(v2)
            #tree.setdefault(v2, []).append(v1)
        return tree

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
        return self[key]

if __name__ == '__main__':
    '''
    Given a List of lists:
    [
        [1,2,3],
        [3,4,5],
        [4,8,9],
        [7,11]
    ]
    Find if there is a route from city 2 to city 11

    '''
    tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
    print (tree.left.right)
    edges = [[1, 2], [1, 3], [2,3],[3, 4], [3, 5], [5, 7], [5, 8]]
    myTree = Tree_List()
    print(myTree.createTreeFromEdges(edges))
