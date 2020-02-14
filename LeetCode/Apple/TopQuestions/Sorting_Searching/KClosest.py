#Approach 1: Sort

#Sorth the points by distance, then take the closest Kpoints

#Time complexity O(N)log(N)
#Space Complexity O(N)
class Solution(object):
    def KCLosest(self,points,K:int)->list:
        points.sort(key=lambda P:P[0]**2+P[1]**2)
        return points[:K]

'''
class Solution
'''
if __name__ == "__main__":
    K = 2
    points = [[3,3],[5,-1],[-2,4]]
    object = Solution()
    print (object.KCLosest(points,K))
