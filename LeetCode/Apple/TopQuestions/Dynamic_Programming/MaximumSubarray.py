#Given an integer array nums, find the contiguous subarray (containing at least
#number) which hast the largest sum and return its sum.


#Example
#Input:[-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6

#Goal is to decide do the drop my first anchor where is my second anchor.
import numpy as np
class Solution:
    def maxSubArray(self,nums) -> int:
        i = 0
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1,n):
            curr_sum = max(nums[i],nums[i]+curr_sum)
            max_sum  = max(curr_sum,max_sum)
        return max_sum


#Divide and Conquer approach
#Graph algorithm
#DC: Divide and Conquer
#Check here
class Solution_DC:
    def cross_sum(self,nums,left,right,p):
        if left==right:
            return nums[left]
        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p,left-1,-1):
            curr_sum +=nums[i]
            left_subsum = max(left_subsum,curr_sum)

        right_subsum = float('-inf')

        for i in range(p+1,right+1):
            curr_sum+=nums[i]
            right_subsum = max(right_subsum,curr_sum)

        return left_subsum+right_subsum


    def helper(self,nums,left,right):
        if left == right:
            return nums[left]
        #middle starting point
        p  = (left+right)//2
        left_sum = self.helper(nums,left,p)
        right_sum = self.helper(nums,p+1,right)
        cross_sum = self.cross_sum(nums,left,right,p)

        return max(left_sum,right_sum,cross_sum)

    def maxSubArray(self,nums)-> 'int':
        return self.helper(nums,0,len(nums)-1)

if __name__ == '__main__':
    nums   = [-2,1,-3,4,-1,2,1,-5,4]
    output = Solution()
    maxSum = output.maxSubArray(nums)
    print ('maxSum is:',maxSum)

    output_DC = Solution_DC()
    maxSum_DC = output_DC.maxSubArray(nums)
    print ('maxSum from Divide and Conquer approach is:',maxSum_DC)


##Now lets implement the Divide and Conquer Solution
