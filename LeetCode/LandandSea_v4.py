'''
A more elegant approach to solving the problem
of counting islands lets take the list
and build a adjacency tree.

Lets say given rectangles: 
'''

class Rectangles():
    def check(self,v,w):
        if w[0][0]>v[0][0] and w[0][1]>v[0][1] and w[1][0]<v[1][0] and w[1][1]<v[1][1]:
            return True
        return False

    def graph(self,rectangles,names):
        graph = {}
        for key,value in rectangles.items():
            graph[key] = set([])

        visited = set()
        for i in range(len(names)-1):
            for j in range(i,len(names)):
                if self.check(rectangles[names[i]],rectangles[names[j]]):
                    graph[names[i]].add(names[j])
        return graph

    #Traverse the tree then count at odd or even number
    #of depth traversal
    def dfs(self,graph,start,visited=None):
        count = 0
        if visited is None:
            visited = set()
        visited.add(start)

        for neighbours in graph[start]-visited:
            self.dfs(graph,neighbours,visited)
            count+=1
        return count

if __name__ == "__main__":
    rectangles = {'A':[(0,0),(10,10)],'B':[(2,1),(5,4)],'C':[(3,2),(4,3)],'D':[(8,4),(9,4)]}
    names = ['A','B','C','D']
    object_Rectangles = Rectangles()
    print ('The connected graph for rectangles is:',object_Rectangles.graph(rectangles,names))

    island_graph = object_Rectangles.graph(rectangles,names)
    print ('The count is:',object_Rectangles.dfs(island_graph,'A'))
