'''
Reference: https://interviewing.io/recordings/Python-Google-12
'''
'''
Question 1:
R B B B G
R B G G R
R B R R G

Find the biggest set of elements in the list
'''

'''
Second Question:
Question 2:
#Check if the sum(left)==sum(right)
#Dynamic Programming
[3 | 1 2] -> true
[1 3 2]  -> true([3 | 1 2])
[2 3 2]   -> false

[3 1 2]
value = left - right #keep track of the imbalancement
initial 0:0
after 1 iteration: -3 (0|3) 3 (3|0)
after 2 itration : -3-> -4  #continue to iterate before we reach 0

Example:
[2 4 2 3 3]
#Let's Dynamic Programming.
#Recursive relationship.
#
'''

from collections import defaultdict
class Solution:
    def partition(self,array):
        default_dict = defaultdict(set)
        default_dict[0].add(0)

        for i,elem in enumerate(array): #we want to have the index and the elementent at the same time
            current = i+1
            for diff in default_dict[current-1]:
                default_dict[current].add(diff-elem) #list #dict--> dict[i]= elem
                default_dict[current].add(diff+elem)
        return 0 in default_dict[len(array)]

#How would we do it without defaultdict?
#[3,1,2]
#1st step:
#1st iteration: left = 0, right= 3
class Solution_2pointers:
    def partition(self,array):
        #one move left, the other move right
        i = 0
        j = len(array)-1
        left = 0
        right = 0
        for i in range(len(array)):
            while (i<j):
                right+= array[j]
                if left==right:
                    return True
                else:
                    left+=array[i]
                j-=1
                i+=1
            return False

'''
Summary:
Problem type:
Public Transportation
Question/s asked:
1) Check whether it is possible to partition an array.
2) Is there a way to get from 1 city to the other with the
given bus routes?

#DFS Algorithm might work.
[
    [1,2,3],
    [3,4,5],
    [4,8,9],
    [7,11]
]
#Find the intersecting elelments between each list in list of lists.
#set -> union. [1,2,3] U [3,4,5] --> [1,2,3,4,5]
'''

'''
Lists of lists
#Thought Patterns.
#1. Find intersecting elements: find intersection. If intersection then
#2. route connection
'''

##BUild Pairs
'''
(0,1)
(0,2)
(0,3)
(1,2)
(1,3)
(2,3)
#Complexity of this algorithm is then:
4C2 --> NC(pairlength) --> NC2
'''
class Solution_City:
    '''
    build_tree hast time complexity of NC2, append is O(1)
    '''

    def build_tree(self,routes):
        #First element of list is 0:
        #Find the intersection, if intersection merge 2 lists of lists:
        #return tree.append(2 lists of lists)
        tree = []
        pairs = [(i,j) for i in range(len(routes)) for j in range(i+1,len(routes))]
        print (pairs)
        for i in range(len(routes)):
            for j in range(i+1,len(routes)):
                if len(set(routes[i]).intersection(set(routes[j]))):
                    tree.append(set(routes[i]).union(set(routes[j])))
        return tree

    #Classical algorithm for iterative merging
    def merge(self,routes):
        merged = []
        anchor = 0
        for i in range(len(routes)):
            for j in range(i+1,len(routes)):
                #Perform elementwise check in both pair list
                for a in range(anchor,len(routes[i])):
                    for b in range(anchor,len(routes[j])):
                        if routes[i][a]==routes[i][b]:
                            anchor = routes[i][a]
                            merged.append(routes[i][:a]+routes[j][b+1:-1])
        return merged

    def isRoute(self,routes,start,goal):
        #Load route.
        #call build tree.
        #Loop over list of lists
        #if start and goal are all in the smae lists, then return lists.
        #which is the path
        merged_routes = routes
        for route in merged_routes:
            if start in route and goal in route:
                return True
        return False

if __name__ == "__main__":
    output = Solution()
    array  = [3, 2,2]
    print ('Is the array partitionable?',output.partition(array))

    output_pointers = Solution_2pointers()
    print ('Is the array partitionable?',output_pointers.partition(array))

    #Second Question 2:
    routes = [[1,2,3],[3,4,5],[4,8,9],[7,11]]
    merged_routes = [[1,2,3,4,5],[1,2,3,4,8,9],[7,11]] #Goal intermediate step
    start = 2
    goal  = 9
    '''
    Expected output: [[1,2,3,4,5],[1,2,3,4,8,9],[7,11]]
    '''
    object = Solution_City()
    print ('The new tree data structure is:',object.build_tree(routes))
    print ('The route exist?:',object.isRoute(merged_routes,start,goal))

    print ('The merged list is:',object.merge(routes))
    #Example start 2: goal: 9
    '''
     1->2->3->4->8->9
    '''























'''
Question 3:
Transportation System:
City A--F--A

2 cities
Bus 1: [1,2,3],
Bus 2: [3,4,5],
Bus 3: [4,8,9],
Bus 4: [7, 11]
Can we travel from 2 to 11?

#Is there a connection from each list of lists?
# Find intersecting elements from each list.
# [1,2,3] -> [3,4,5] -> [4,8,9] -> [7,11]
# union join all the lists
Bus1 union join 1 ->

#Find the shortest number of bus changes?
#
'''
