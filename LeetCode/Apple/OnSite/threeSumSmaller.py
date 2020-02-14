'''
Given an array of n integers nums and a target, find the number
of index triplets i, j, k with 0 <= i < j < k < n that
satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:
Input:
'''
class Solution:
    def hash(self,nums):
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        return hashmap

    def complement_map(self,nums,target):
        complement_map = {}
        for num in nums:
            complement_map[num]= target-num
        return complement_map

    def threeSumSmaller(self,nums,target):
        #In Brute force we would have a computational Complexity
        #of n^3
        #we reduce the computtional complexity to on²
        #Search for the hashmap
        #complement_map is a dict:
        complement_map = self.complement_map(nums,target)
        #Keep track of indices:
        index = []
        k=1
        for i in range(len(nums)):
            for j in range(1,len(nums)-k):
                if nums[i] < target and nums[j] < target: #if the numbers are greater
                #than the target- ignore them.
                    if nums[j]+nums[j+k]<complement_map[nums[i]]:
                        index.append(nums[i])
                        index.append(nums[j])
                        index.append(nums[j+k])
                        #k+=1
        return index
#Another approach 2 pointers.
#Divide and ocnquer approach: Start from both side.


#2 Pointers approach
#sort array of length n: nlogn
#perform binary search from the middle. --> such that sum = target - nums[i]
#
class Solution_2pointers:
    def threeSumSmaller(self,nums,target):
        sum = 0
        #sort the array.
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-2):
            sum+=self.twoSumSumaller(sorted_nums,i+1,target-sorted_nums[i])
        return sum

    #We first work on twoSumSumaller.
    #we use 2 pointers from right and left.
    def twoSumSumaller(self,nums,startindex,target):
        sum = 0
        left = startindex
        right = len(nums)-1 #since we want to index the array
        #We have 2 pointers left and right.
        #we do not allow tot croos over
        while (left <right):
            #we move left to more right.
            #we move right to more left.
            if (nums[left]+nums[right])<target:
                sum +=right-left
                left+=1
            else:
                right -=1
        return sum

'''
Here the time complexity is: O(n)*log(n)*n --> O(n²log(n))
Space Complexity: O(1)
'''

if __name__ == "__main__":
    nums = [3,5,2,8,1]
    target = 9
    object = Solution()
    print ('The complement_map is:',object.complement_map(nums,target))
    print ('The sum combinations are:',object.threeSumSmaller(nums,target))

    object_2pointers = Solution_2pointers()
    print ('The sum combinations are:',object_2pointers.threeSumSmaller(nums,target))
