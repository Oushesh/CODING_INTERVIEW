#Reference: https://www.youtube.com/watch?v=j7DjJm2eKbs

'''
Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum is the target. Example target is 15
'''

'''
Similar question to the one here: LinkedInEngineerSecondTime_TwoSum_Continuous_Subarray.py
'''

'''
Example: numbers = [1,2,3,4,5,6,7,8,9,10], target = 15,
         cum = [1,3,6,10,15...] --> 1st condition met.
         [4, 5, 2, 3,7,5], target = 12 --> (1,3)
         [4, 9, 11,14] sum > target: True
         sum - target = 14-12 = 2, j=0, 14==4: False
     else: update j: j+=1, list[j]--> 5, target = 12
         shift+1, list is now: [5,2,3,7], sum_list = [5,7,10,17] update sum = 17, 17-12 = 5.
         sum - target == 14 -
'''
from functools import reduce

#To reduce: skills:
class PatternMatch:
    def search(self, list, target):
        sum = 0
        count = 0
        j = 0
        for i in range(len(list)):
            if list[i]==target:
                count +=1
            elif sum <=target:
                sum+=list[i]
                if sum==target:
                    count+=1
            if sum>target:
                '''
                #here cum_sum > target --> we need to remove the elements from before
                '''
                while sum>target:
                    print ('sum',sum)
                    if (sum-target)==list[j]:
                        count +=1
                    else:
                        #we skip the first elemeent on the list from the left
                        #to right, move j
                        #update the sum list.
                        j+=1
                        print (list[j])
                        print (i,j)
                        sum = reduce(lambda x,y:y+x,list[j:i+1])
        return count

#TODEBUG
if __name__ == '__main__':
    #numbers = [1,2,3,4,5,6,7,8,9,10]
    #target = 15

    numbers  = [4,5,2,3,7,5]
    #cum_sum = [4,9,11,14,...]
    target = 12
    count = PatternMatch()
    print ('The total number of continuous subarrays whose sum is the target is',count.search(numbers,target))
