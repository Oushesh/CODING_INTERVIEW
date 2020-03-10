'''
Let's say we have a list of rectangles
of names 'a', 'b', 'c', 'd'
'''

class Rectangle:
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

    def build_combination(self,nodes):
        '''
        Input: Dict of rectangles
        example: ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        output : [['a','b'],['b','c'],['c','d'],['d','e'],['e','f'],['f','g'],['g','h'],['h','i'],
        ['i','j'],['j','k'],['k','l'],['l','m'],['m','n']]
        'if we do not have ordered data: then build all possible pairs'
        '''

        nodes = list(rectangles.keys())
        combination = []
        for i in range(len(nodes)-1):
            for j in range(i+1,len(nodes)):
                combination.append([nodes[i],nodes[j]])
        return combination

    def overlap_combination(self,combinations,rectangles):
        '''
        combinations: List[List] containing the keys (str) name of function
        rtype: List[List]
        '''
        overlaped_combinations = []
        for combination in combinations:
            if self.line_overlap(rectangles[combination[0]],rectangles[combination[1]])==1:
                overlaped_combinations.append(combination)
                #combinations.remove(combination)
            else:
                print ('not overlap',combination)
        return overlaped_combinations


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

    '''
    rectangles = ['a','b','c','d']
    #all possible pairs are then:
    ['a','b'], ['a','c'],['a','d'], ['b','c'],['b','d'],['c','d']
    Run intersection and we find a new list of edges:
    ['a','b'] 'c']
    '''

    edges = [[1, 2], [2,3],[3, 4], [3, 5], [5, 7], [5, 8]]
    myTree = Rectangle()
    print(myTree.createTreeFromEdges(edges))

    situation1 = [['a','b'],['a','c'],['b','c']]
    situation2 = [['a','b'],['a','c']]

    print (myTree.createTreeFromEdges(situation1))

    print (myTree.createTreeFromEdges(situation2))


    rectangles = {'a':[1,1,6,10],
    'b':[2,2,5,4],
    'c':[3,2.5,4,3.5],
    'd': [5,7,9,11],
    'e':[6,8,9,10]}

    combinations = myTree.build_combination(rectangles)
    print ('edge combinations are:',combinations)
    '''
    >>> a=[1,2,3]
    >>> a.remove(2)
    >>> a
    [1, 3]
    >>> a=[1,2,3]
    >>> del a[1]
    >>> a
    [1, 3]
    >>> a= [1,2,3]
    >>> a.pop(1)
    2
    >>> a
    [1, 3]
    >>>
    '''
    overlaped_combinations = myTree.overlap_combination(combinations,rectangles)
    print ('resulting combinations are overlap :',overlaped_combinations)

    print ('The rectangle tree combination is:',myTree.createTreeFromEdges(overlaped_combinations))
    print ('test overlap',myTree.line_overlap([3,2.5,4,3.5],[5,7,9,11]))
