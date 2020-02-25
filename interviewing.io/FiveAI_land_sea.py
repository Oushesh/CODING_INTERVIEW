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
        children
        '''
        for key,value in graph.items():
            if len(value)==1:
                if node == value:
                    return key
            elif len(value)>1:
                if node[0] in value:
                    print(key)
                    return key

    def build_connection(self,rects):
        '''
        rects: List of Lists
        how do we build the dict? lets use a dict of lists:
        tree = {a:[b,c],b:[d,e],etc..}
        '''
        graph  = {}
        for rect in rects:
            '''
            rect is a list:[x1,y1,x2,y2]
            '''
            graph[a] = []
            if self.find_full_overlap(a,b):
                graph[a] +=[b]  #use the fact that in python you add all the elements to append to list
            else:
                '''
                recursively move up the tree to query parent
                of the current parent --> b
                and find the parent recusively until
                we reach main parent node
                '''
                while (not self.find_full_overlap(a,b)):
                    b = self.parent(graph,b) #get the parent of b
        return graph

    def count_sea(self,tree):
        '''
        tree: {a:[b,c],b:[d,e],e:[f,g]} dict of Lists, Lists are the children
        rtype: num_sea: integer
        '''
        num_sea = 0
        for :
        return num_sea


if __name__ == "__main__":
    '''
    Find the minimum in the dataset and start
    or sort the data. Assumption
    '''
    a = [1.0, 1.0, 10.0, 6.0]
    b  = [1.5, 1.5, 6.0, 5.0]
    object = Solution()
    print (object.find_full_overlap(a,b))
    '''
    'TODO: change data structure to a dict'
    {'a':[1,2,3,4],'b':}
    '''
