#1.TwoSum
#Brute Force
class Solution:
    def twoSum(self,nums,target):
        output = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                if (nums[i]==target-nums[j]):
                    output.append(nums[i])
                    output.append(nums[j])
        return output


#Interviewer will ask:
#Space Compltexity : O(1)
#time complexity: O(n²-n) ~ o(n²)

#Using a Hash Technique:
#As a rule of thumb to decrase time
#complexity, we can only precompute results
#from the hash table

class Solution_Hash:
    def twoSumHash(self,nums,target):
        Hash = {}
        for i in (nums):
            if (target-i) not in Hash:
                Hash[i]  = target-i
            return [i,Hash[i]]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target  = 9
    object = Solution()
    output = object.twoSum(nums,target)
    print (output)

    object_Hash = Solution_Hash()
    output_Hash = object_Hash.twoSumHash(nums,target)
    print (output_Hash)
