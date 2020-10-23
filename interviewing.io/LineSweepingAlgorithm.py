'''
Line Sweeping Algorithms in Mathematics:
1. Find min(x),max(x):
2. Loop over x-coordinate from min(x) to max(x)
3. Increments of 0.5
4. At each iteration: find if x-coordinate is in the rectangles dict-List

open = {'a','b','c'}
close = {'c','b','a'}

5. if found:
    add the name to open dict.
    in each iteration, if overlap --> True. add the dict as
'''

class LineSweeping():
    def sort(self,rectangles):
        '''
        rectangles: dict of List
        rtype: dict of List
        '''
        sorted_dict = {}
        for key,value in sorted(rectangles.items()):
            sorted_dict[key] = value
        return sorted_dict

    def line_overlap(self,a,b):
        '''
        a: List [x1,y1,x2,y2]
        b: List[x1,y1,x2,y2]
        rtype: overlapped or not: boolean variable
        y1 of b > y1 of a.
        y2 of b < y1 of a
        '''
        if (b[1]>a[1]) and (b[3]<a[3]):
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

    def linecount(self,rectangles):
        count = 0
        open = {}
        close = {} #keep track of closing edge of rectangles
        sorted_rectangles = self.sort(rectangles)

        min_x = min([x[0] for x in sorted_rectangles.values()])
        max_x = max(x[2] for x in sorted_rectangles.values())
        '''
        Move the sweeping line over the rectangles:
        '''
        #Build a range of values for 0.5 step
        value_range = [x*0.5 for x in range(int(2*min_x),int(2*max_x+1))]

        for x in value_range: #move from min_x to max_x in steps of 0.5
            for rect_name,rect_coordinate in sorted_rectangles.items():

                if x == rect_coordinate[0] and len(open)==0:
                    open[' '] = rect_name
                    #open.append(rectangle)

                elif x == rect_coordinate[0] and len(open)>0: #we already encountered something before
                    '''
                    Find overlap between current line and all in the open dict
                    '''
                    for parent, children in open.items():
                        if children:
                            if self.line_overlap(rect_coordinate,sorted_rectangles[children]):
                                open[children] = [rect_name]
                                print (open)
                            else:  #noverlap
                                #Query the parent of the current node in the tree
                                while (self.parent(open,children)):
                                    children = self.parent(open,children)
                                open[key] 
                                open[key] +=[children]
            print (open)
        return len(open)

if __name__ == "__main__":
    rectangles = {'a':[1,1,6,10],
    'b':[2,2,5,4],
    'c':[3,2.5,4,3.5],
    'd': [5,7,9,11]}
    solution = LineSweeping()
    sorted_rectangles = solution.sort(rectangles)
    print ('sorted rectangles:',sorted_rectangles)
    print(solution.linecount(rectangles))
