'''
Releference: https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2868/
Merge Sort Algorithm
'''

'''
list.extend from python library:
'''
class Solution:
    def merge_sort(self,nums):
        #edge cases if list is empty or has only elment
        if len(num) <=1:
            return nums

        pivot = int(len(nums)/2)
        left_list = merge_sort(nums[0:pivot])
        right_list = merge_sort(nums[pivot:])
        return merge(left_list, right_list)

    def merge(self,left_list,right_list):
        left_cursor = right_cursor = 0
        ret  = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor +=1
            else:
                ret.append(right_list[right_cursor])
                right_cursor +=1

        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])
        return ret

if __name__ == "__main__":
    numbers = [-1,5,2,6,7,3,1]
    current_Solution = Solution()
    print ('The sorted array based on divide and conquer approach is:',current_Solution.merge_sort(numbers))
