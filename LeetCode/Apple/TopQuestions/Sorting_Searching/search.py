#Algorithm run on log(n)
#Brute force: search over all of the array:

#Approach 2: we know array is rotated:
#First step is to find the rotation pivot.
#Go in the middle--> given we know array
#is in ascending order --> left of my pivot less,
#right high--> if this is true. I go left or right.
#Given we know there is only 1 rotation--> greedy Approach
#First index where the condition breaks is pivot.

class Solution:
    def search(self,nums,target) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    output = Solution()
    print (output.search(nums,target))
