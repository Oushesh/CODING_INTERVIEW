class Solution:
    def subsets(self,nums):
        #edge case
        if nums is None or len(nums)==0:
            return None
        res = [[]]
        for num in nums:
            n=len(res)
            for i in range(n):
                res.append(res[i]+[num])
        return res

#Time Complexity: O(len(num)*)
#Space Complesity: O(1)O()

if __name__ == "__main__":
    nums = [1,2,3]
    output = Solution()
    print ("The subsets are:",output.subsets(nums))
