'''
Apple online interview:
448. Find all nummbers Disapperared in an Array.
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

class Solution:
    def findDisappearedNumbers(self, nums):
        #First sort the array, what kind of data does this return a lsit?
        output = []
        for i in range(len(nums)):
            if i not in sorted(nums):
                output.append(i)
        return output


#Using set data structure from Python
#its faster why?
class Solution_Set:
    def findDisappearedNumbers(self,nums):
        if len(nums) > 0:
            return set(range(1,len(nums)+1))-set(nums)
        else:
            return []

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    output  = Solution()
    print ("The disappeared numbers are:",output.findDisappearedNumbers(nums))

    output_set = Solution_Set()
    print ("The disappeared numbers are:",output_set.findDisappearedNumbers(nums))
