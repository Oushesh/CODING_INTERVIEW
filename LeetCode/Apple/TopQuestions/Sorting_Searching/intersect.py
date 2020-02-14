#Given 2 arrays, write a function to compute
#their intersection.


#Example 1:
#Input: nus1=[1,2,2,1]
#nums2= [2,2]
#OUtput: [2,3]


#Example 2:
#Input: nums1=[4,9,5]
#nums2: [9,4,9,8,4]
#Output: [4,9]


#Follow Up Questions:
#What if the given array is already srted?
#How would you optimize your algorithm?
#What if num1's size is small compard to num2's size
#? Which algorithm is better?

#WHat if elements of nums2 are sorted on disk,
#and the memory is limited such that you cannot
#load all elements into the memory
#at once?



#Ideas how to proceed:
#compare length of 2 strings
#take the longer one
#Build a frequency hash map

#Compare the elements of the second array
#with the frequency h

class Solution(object):
    def hashmap(self,num):
        #How to build a hash map??
        dict = {}
        for i in num:
            if i not in dict:
                dict[i]=1
            elif i in dict:
                dict[i]+=1
        return dict

    def intersect(self,nums1,nums2):
        common = []
        if len(nums1)>len(nums2):
            #Build hashmap
            dictionary = self.hashmap(nums1)
            for i in nums2:
                if i in dictionary and dictionary[i]!=0:
                    dictionary[i]-=1
                    if i not in common:
                        common.append(i)
        else:
            dictionary=self.hashmap(nums2)
            for i in nums1:
                if i in dictionary and dictionary[i]!=0:
                    dictionary[i]-=1
                    if i not in common:
                        common.append(i)
        return common

if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    output = Solution()
    print ('The intersecting elements are:',output.intersect(nums1,nums2))


    nums3 = [1,2,2,1]
    nums4 = [2,2]
    print ('The intersecting elements are:',output.intersect(nums3,nums4))
