'''
Permutations
Given a collection of distinct integers, return all possible
permutations.

Example:

Input: [1,2,3]
Ouput:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

pivot = o
rest
swap(rest)
output = pivot + 2 possibilities of rest

make the next digit as pivot:
append pivot.
'''

class Solution:
    def swap(self,sublist):
        assert(len(sublist)==2)
        sublist [0], sublist[1] = sublist[1],sublist[0]
        return sublist

    def permute(self,nums):
        #set the pivot
        #swap remaining
        #lets work with indices
        pivot = nums[0]
        output = []
        for i in range(len(nums)):
            pivot = nums[i]
            rest = [nums[j] for j in range(len(nums)) if j!=i]
            output.append([pivot]+rest)
            #swapped takes in all elements except pivot
            swapped = self.swap(rest)
            output.append([pivot]+swapped)
        return output

class Solution_optimized:
    def hash(self,nums):
        '''
        nums:List[int]
        '''
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i]=[k for k in nums if k!=i]
        return hash_map
        #Key reperesents the pivot, value represents the rest

    def swap(self,sublist):
        assert(len(sublist)==2)
        sublist [0], sublist[1] = sublist[1], sublist[0]
        return sublist

    def permute(self,nums):
        output = []
        hash_map = self.hash(nums)
        for i in range(len(nums)):
            pivot = nums[i]
            rest = hash_map[nums[i]]
            output.append([pivot]+rest)
            swapped = self.swap(rest)
            output.append([pivot]+swapped)
        return output

'''
INterviewer asks me:
Time Complexity:
We have  a list <int> of length(n), We loop over it only once:
we build rest list: O(n-1). swap function, O(1) time. append element: O(1)
We have time complexity O(n(n-1))~O(n²)

Can we do better? Yes. We can build a hash table for each index at pivot, we
save the rest. as dictionary. Then we perform lookup. Then we have O(n)

#Space Time Complexity Analysis:
#Constant pivot, output: n! list in our list

#WHat about other methods?
'''

class Solution_Backtracking:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


#Time Complexity here:

if __name__ == "__main__":
    nums = [1,2,3]
    output = Solution()
    print ('The permutations are:',output.permute(nums))

    output_optimized = Solution_optimized()
    print ('The permutations from optimized solution are:',output_optimized.permute(nums))

    output_backtracking = Solution_Backtracking()
    print ('The permutations from the backtracking solutions are:',output_backtracking.permute(nums))
