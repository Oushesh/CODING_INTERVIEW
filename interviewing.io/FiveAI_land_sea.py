'''
Preliminary Given Data:
14
1.0 1.0 10.0 6.0
1.5 1.5 6.0 5.0
2.0 2.0 3.0 3.0
2.0 3.5 3.0 4.5
3.5 2.0 5.5 4.5
4.0 3.5 5.0 4.0
4.0 2.5 5.0 3.0
7.0 3.0 9.5 5.5
7.5 4.0 8.0 5.0
8.5 3.5 9.0 4.5
3.0 7.0 8.0 10.0
5.0 7.5 7.5 9.5
5.5 8.0 6.0 9.0
6.5 8.0 7.0 9.0

Sample output:
9
'''


'''
Input Data structure: (x1,y1,x2,y2)
x1:lower corner x coordinate
y1: lower corner y coordinate
x2: upper corner x coordinate
y2: upper corner y coordinate

What do we have in this problem?:
List of Lists
a List of 4 float values
[x1,y1,x2,y2]
For each pair of the list and assuming no 2
So I have the algorithm here.
'''

class Solution:
    def find_full_overlap(self,a,b):
        '''
        a: List [x1,y1,x2,y2]
        b: List[x1,y1,x2,y2]
        rtype: overlapped or not: boolean variable
        x1,y1 of b > x1,y1 of a.
        x2,y2 of b < x1,y1 of a
        '''
        if (b[0]>a[0] and b[1]>a[1]) and (b[2]<a[2] and b[3]<a[3]):
            return 1
        return -1

    def parent(self,graph,node):
        '''
        node as a single list element or List itself in case of multiple
        children there and recover.
        '''
        for key,value in graph.items():
            if len(value)==1:
                if [node] == value:
                    return key
            elif len(value)>1:
                if node[0] in value:
                    return key
            else:
                return -1 #no parent is found

    #check this function
    #
    def build_connection(self,rectangles):
        '''
        rects: List of Lists
        how do we build the dict? lets use a dict of lists:
        tree = {a:[b,c],b:[d,e],etc..}
        '''
        graph  = {}
        #check this loop once more.
        for i in range(len(rectangles.keys())-2):
            parent      = list(rectangles.keys())[i] #access via index
            graph[parent] = []
            child       = list(rectangles.keys())[i+1]
            #print (graph)
            if self.find_full_overlap(rectangles[parent],rectangles[child])==1: #pairwise checking
                graph[parent]  += [child]
                parent      = list(rectangles.keys())[i+1] #update parent to child
                child          =  list(rectangles.keys())[i+2]
                print (parent)
                print (child)
                print (graph)
            while (self.find_full_overlap(rectangles[parent],rectangles[child])==-1 and self.parent(graph,parent)!=-1):
                '''
                recursively move up the tree to query parent
                of the current parent --> b
                and find the parent recusively until
                we reach main parent node
                '''
                #query the parent of parent
                parent = self.parent(graph,parent)
                print ('query parent',parent)
        return graph

'''
Final Result: graph = {'a':['b','h'],'b':['c','d','e'],'e':['f','g'],'h':['i','j'],'k':['l'],'l':['m','n']}
'''

if __name__ == "__main__":
    rectangles = {'a':[1.0, 1.0, 10.0, 6.0],
    'b':[1.5, 1.5, 6.0, 5.0],
    'c':[2.0, 2.0, 3.0, 3.0],
    'd':[2.0, 3.5, 3.0, 4.5],
    'e':[3.5, 2.0, 5.5, 4.5],
    'f':[4.0, 3.5, 5.0, 4.0],
    'g':[4.0, 2.5, 5.0, 3.0],
    'h':[7.0, 3.0, 9.5, 5.5],
    'i':[7.5, 4.0, 8.0, 5.0],
    'j':[8.5, 3.5, 9.0, 4.5],
    'k':[3.0, 7.0, 8.0, 10.0],
    'l':[5.0, 7.5, 7.5, 9.5],
    'm':[5.5, 8.0, 6.0, 9.0],
    'n':[6.5, 8.0, 7.0, 9.0]}

    output = Solution()
    graph=output.build_connection(rectangles)
    print (graph)


    node={'a':['b','h'],'b':['e'],'e':['f','g'],'h':['i','j'],'k':['l'],'l':['m','n']}
    print ('test parent function',output.parent(node,'e'))
