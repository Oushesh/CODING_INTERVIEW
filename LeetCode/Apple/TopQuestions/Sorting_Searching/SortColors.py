#Given an array with n colored red,white
#or blue, sort them in-place so that the
#boejcts of the same corlor are adjacetn,


#Follow up:
#Given an array with n objects red, white or blue,
#sort them in-place so that objects of
#red, white and blue respectively.

#Input: [2,0,2,1,1,0]
#OUtput: [0,0,1,1,2,2]

from collections import OrderedDict
class Solution:
    def sortColors(self,nums):
        return (sorted(nums))

#hash table O(nlogn)
#query key which is o,1 -> freuqnevy
#decrease by one then move the

class Solution_custom:
    def hashmap(self,nums):
        dict = {}
        for i in (nums):
            if i not in dict:
                dict[i]=1
            elif i in dict:
                dict[i]+=1
        return dict

    def sortColors(self,nums):
        output = []
        dict = self.hashmap(nums)
        #sort according to key
        ordered_dict={k: v for k, v in sorted(dict.items(), key=lambda item: item[0])}
        
        for i in ordered_dict:
            while ordered_dict[i]!=0:
                output.append(i)
                ordered_dict[i]-=1
        return output
#O(nLogN) -->Hashmap is just O(n)

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    output = Solution()
    print (output.sortColors(nums))

    output_custom = Solution_custom()
    print (output_custom.sortColors(nums))
