#test the code:
class Solution():
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

    def build_combination(self,nodes):
        '''
        Input: Dict of rectangles
        example: ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        output : [['a','b'],['b','c'],['c','d'],['d','e'],['e','f'],['f','g'],['g','h'],['h','i'],
        ['i','j'],['j','k'],['k','l'],['l','m'],['m','n']]
        'if we do not have ordered data: then build all possible pairs'
        '''
        #nodes = list(rectangles.keys())
        combination = []
        for i in range(len(nodes)-1):
            for j in range(i+1,len(nodes)):
                combination.append([nodes[i],nodes[j]])
        return combination

    def check_overlap(self,input_list):
        '''
        Input:
        check overlap and return only the valid pairs
        return list of string containing the names
        '''
        output_pairs = []
        for pairs in combinations:
            if (self.find_full_overlap(pairs[0],pairs[1])):
                output_pairs.append(pairs)
        return output_pairs

    def edge2Tree(self,edges):
        '''
        tree: list of lists edges
        List connections only once.
        '''
        tree  = {}
        for i in edges:
            v1,v2 = i
            if v1 in tree:
                tree[v1].append(v2)
            else:
                tree[v1] = [v2]
        return tree

graph = {'a':['b','h'],'b':['c','d','e'],'e':['f','g'],'h':['i','j'],'k':['l'],'l':['m','n']}
graph_list = list(graph.items())
for i in range(len(graph_list)-1):
    print ('current',graph_list[i])
    print ('next',graph_list[i+1])

if __name__ == "__main__":
    '''
    Lets say we have edges which is a list of list:
    Lets add some order in the tree:
    First element: is the parent, second one is the child
    [[parent1,child1],[parent1,child2], etc..]]
    '''
    rectangles = [[1.0, 1.0, 10.0, 6.0],
    [1.5, 1.5, 6.0, 5.0],
    [2.0, 2.0, 3.0, 3.0],
    [2.0, 3.5, 3.0, 4.5],
    [3.5, 2.0, 5.5, 4.5],
    [4.0, 3.5, 5.0, 4.0],
    [4.0, 2.5, 5.0, 3.0],
    [7.0, 3.0, 9.5, 5.5],
    [7.5, 4.0, 8.0, 5.0],
    [8.5, 3.5, 9.0, 4.5],
    [3.0, 7.0, 8.0, 10.0],
    [5.0, 7.5, 7.5, 9.5],
    [5.5, 8.0, 6.0, 9.0],
    [6.5, 8.0, 7.0, 9.0]]
    #nodes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    #edges = [['a','b'],['a','h'],['b','c'],['b','d'],['b','e'],['e','f'],['e','g'],['h','i'],['h','j'],['k','l'],['l','m'],['l','n']]
    current_output = Solution()
    combinations = current_output.build_combination(rectangles)
    #print ('combinations are:',combinations)
    intersecting_combinations = current_output.check_overlap(combinations)
    print (len())
    print ('intersecting pairs:',intersecting_combinations)


    print ('tree is',current_output.edge2Tree(edges))
