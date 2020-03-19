'''
Dynamic Programming Question.
'''
#INterview Question:
#Leetcode

#Dynamic Problem Question
#O(n²) --> Brute Force Solution
#Dynamic Problem solution:
'''
For example we have:
[-2,-3,4,1,-2,1,5,-3]
max Subarray = [4,-1,-2,5]
#Lets look at the problem stepwise
Initially: max = -inf., currSum = 0
[-2] --> max = -2, currSum = -2
[-2,-3] --> max = [-2] ,curSum = -2 - 3 = -5
[-2,-3,4] --> max = 4, curSum = -2 - 4 + 4 = -1
[-2,-3,4,1,-2] --> max = - 2+4+4 =-1
'''

class Solution():
    def maxSubarray(self,numbers):
        #start_index = 0
        end_index   = 1
        maxsoFar    = numbers[0]
        sum         = [0 for i in range(len(numbers))]
        for i in range(len(numbers)):
            if numbers[i] > 0:
                start_index = i
                for j in range(i,len(numbers)):
                    sum[j]  = sum[j-1] + numbers[j] #build the sum
                    maxsoFar = max(maxsoFar,sum[j])
        return maxsoFar

if __name__ == "__main__":
    numbers = [-2,-3,4,1,-2,1,5,-3]
    output = Solution()
    print ('The maximum subarray is:',output.maxSubarray(numbers)[0])
