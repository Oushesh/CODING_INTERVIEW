'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-on-site-for-sde/

Suppose you have an array consisting of 0 and 1. Find the total number
of subarrays of 0 & also output the possible outcomes


Example: Input:  [0,0,1,0,1]
         Output: [0,0,00,0]


Pseudo Code:
Time Complexity: O(n) We loop only once in worst case
Space Complexity: let see


1. Loop over the entire array,count = 0
2. Count 0: if the array[idx]==0
   output.append(array[idx]), count+=1


   Recursive update, ask the interviewer: what if we have 3 consecutive 0s
                            if the current is 0:
                                output.append([array[idx]])
   Explanation:      000 --> [0],count=1, count+=1
                         --> [0,0], count=2, count+=1
                         --> [0,0,0]
                         output.append([],[0])

    number of consecutive zeros: 3 000 --> 0,0,0, 00, 00, (3 singlets,  2 doubles, 1 triplets)

                                 4 0000 --> 0,0,0,0 (4 singlets, 3 duplets, 2 triplets, 1 quadruplets)
                                 5 00000 --> (5 singlets, 4 duplets, 3 triplets, 2 quadruplets, 1 cinquets)




1. Loop over the array.
2. if we find zero we continue on:
     until we dont find zeros or we reach end of array.
     update the zero_count. we break the condition there.

'''
class zero_count():
    def combinations(self,zeros):
        '''
        This function derives the logic behind the number
        of zeros to get the number of combinations.
        Triangular numbers.
        5 ---> 5+4+3+2+1....
        '''
        sum = 0
        while zeros <=1:
            sum+=zeros
            zeros-=1
        return zeros

    def subaary_count(self,array):
        subarray_count = 0
        zeros = 0
        idx = 0
        for i in range(len(array)):
            if idx>0 and idx <=len(array):
                while array[idx]==0:
                    idx+=1
                    zeros+=1
                subaary_count+=self.combinations(zeros,subarray_count)
        return subaary_count


if __name__ == "__main__":
    array = [0,0,1,0,1]
    current_zero_count = zero_count()
    print ('The number of zero combination here is:', current_zero_count.subaary_count(array))

'''
Unreal Engine:https://www.youtube.com/results?search_query=siren+free+lateral
Thibault  Weiss manager munich
'''
