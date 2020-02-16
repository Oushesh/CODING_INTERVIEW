'''
Reference video to coding video:
https://www.youtube.com/watch?v=KpIVsxswZLo
Techincal Interview with a Microsoft engineer: K closest points
'''

'''
List of points:
List[List]: x,y
np.float distance
int k= 10: 10 closest points to the integer.
Point: vertex: (x,y)

Edge Case: Assume that we have 10 points and if we have less
then 10 points we return all the points.

Brute Force Approach:
N points, 1 Vertex.
Compute distance between all point pairs. --> Array Looping: N
Compute distance np.sqrt(point_n,vertex)
save all the distances: Space complexity O(n)
#sort this array: O(nlog(n)) --> average case
#O(n²)log(n) --> computational complexity
O(n) --> spatial complexity
'''

import numpy as np
import math
class Solution:
    def distance(self,points,vertex):
        '''
        points: List[List]
        vertex: List #x,y coordinates
        rtype: List
        '''
        distances = []
        for i in points:
            distances.append(np.sqrt((i[0]-vertex[0])**2+(i[1]-vertex[1])**2))
        return distances

    #Define sorted points based on distance
    def sort(self,points,distances,k):
        '''
        points: List
        rtype: List
        sort based on the distances keep track of original index
        How to keep track of old indices?
        '''
        sorted_index_pos = [index for index, num in sorted(enumerate(distances), key=lambda x: x[-1])]
        return [points[i] for i in sorted_index_pos][:k]

'''
Can we make this better? Yes
Lets make a queue K entries.
As we loop over the points:
    compute the distance.
    (2 pointers one left and one right)
    Put the first one on the far left. Lowest distance
    if next element is less than first put element far right
    if element less than far right right, put element right-1
Priority Queue:
'''
class Solution_Opimized:
    def distance(self,point,vertex):
        '''
        points: List x,y
        vertex: List #x,y coordinates
        rtype: float
        '''
        return np.sqrt((point[0]-vertex[0])**2+(point[1]-vertex[1])**2)

    #Build the priority queue
    def priority_queue(self,points,vertex,k):
        queue = []
        distances = []
        for i in points:
            '''
            calculate euclidean distance here:
            '''
            if len(queue)<=k:
                queue.append(i)
                sorted(queue,key = lambda point:self.distance(point,vertex)) #returns a sorted list
            else:
                '''
                cross check against all elements in the queue
                compare distance against distances
                '''
                for j in range(len(queue)):
                    if self.distance(i,vertex) < self.distance(queue[j],vertex):
                        #overwrite the queue and update the queue
                        queue.insert(j,i) #insert i at position j
                        print ('queue',queue)
                        queue.pop()
        return queue
'''
def distance_squared(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2
target_point = 0,0

a = [[1,5],[1,2],[-1,1]]
print (sorted(a,key=lambda point:distance_squared(target_point[0],target_point[1],point[0],point[1])))
'''

if __name__ == "__main__":
    k      = 2
    vertex = [2,3]
    points = [[1,5],[1,2],[-1,1]]
    mySolution = Solution()
    distances = mySolution.distance(points,vertex)
    print (distances)
    print ('sorted_points:',mySolution.sort(points,distances,k))

    mySolution_Optimized = Solution_Opimized()
    mySolution_Optimized.priority_queue(points,vertex,k)

    print ('optimized sorted points:',mySolution_Optimized.priority_queue(points,vertex,k))
