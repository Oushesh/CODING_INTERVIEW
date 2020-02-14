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
            tree.setdefault(v2, []).append(v1)
        return tree

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
        return self[key]

    def routes2edges(self,routes):
        #First step take in lists of Lists from routes.
        #return edges
        edges = []
        for route in routes:
            parent = route[0]
            for j in range(1,len(route)):
                edges.append([parent]+[route[j]])
        return edges

'''
Pseduo Code: Breadth First Search:
BFS(Q:Graph,S: source node)
BFS:
    BFS (G, s)                   //Where G is the graph and s is the source node
      let Q be queue.
      Q.enqueue( s ) //Inserting s in queue until all its neighbour vertices are marked.

      mark s as visited.
      while ( Q is not empty)
           //Removing that vertex from queue,whose neighbour will be visited now
           v  =  Q.dequeue( )

          //processing all the neighbours of v
          for all neighbours w of v in Graph G
               if w is not visited
                        Q.enqueue( w )             //Stores w in Q to further visit its neighbour
                        mark w as visited.
                        https://www.hackerearth.com/de/practice/algorithms/graphs/breadth-first-search/tutorial/
'''

class route:
    def BFS(self,graph,start,goal):
        '''
        1. build the edges from the routes
        2. build the tree struture
        3. returns a boolean variable whether the route exists or not.
        4. Traverse down the tree. breeath first search

        Tree Structure is a dictionary: {1: [2, 3], 2: [1], 3: [1, 4, 5], 4: [3], 5: [3, 7, 8], 7: [5], 8: [5]}
        '''
        #keep track of all visited nodes
        explored  = []
        #keep track of nodes to be checked
        queue     = [start]
        #keep looping until there are still nodes to be checked
        while queue:
            #pop shallowst node.
            node  = queue.pop(0)
            if node not in explored:
                #add node to list of checked nodes
                explored.append(node)
                neighbours = graph[node]
                #add neighbours/children to node of quque
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored


if __name__ == '__main__':
    tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
    print (tree.left.right)
    '''
    routes = [[1,2,3],[3,4,5],[5,7,8]]
    Lets draw this:
      1
    /   \
    2   3
       / \
       4  5
          / \
         8   7
    Convert to the structure:
    myTree = [1,2,3] #oR the other structure:
    myTree = [1,[2,[],[]],[3,4,5]]

    Way 1: Take in Routes as trees and build the edges
    From the edges build a tree structure: Lists of lists
    We have a tree structure which gives us,
    '''
    myTree = Tree_List()
    routes = [[1,2,3],[3,4,5],[5,7,8]]
    edges  = myTree.routes2edges(routes)
    print ('The edges from the routes are:',edges)
    #edges = [[1, 2], [1, 3], [3, 4], [3, 5], [5, 7], [5, 8]]
    print('The tree structure is thus,',myTree.createTreeFromEdges(edges))


    #Now lets see how do we perform the binsry tree search
    myRoute = route()
    print ('The explored pathway is',myRoute.BFS(myTree.createTreeFromEdges(edges),3,8))
