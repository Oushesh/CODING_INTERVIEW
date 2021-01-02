#Reference: https://www.youtube.com/watch?v=psQ2lpH2hMQ
#https://www.youtube.com/watch?v=psQ2lpH2hMQ

#TODO: Complete this interview. its one of the easiest here.



'''

1. Reverse 32 bit signed integer. Then reverse it. -->

123 --> 321
-123 --> -321
#https://www.youtube.com/watch?v=NXaVLXSZdEw Three Sum


#This is super easy. Lets think about what if we would have:
#Two Sum then afterwards the Three Sum. Two Sum: Complement[number] --> the remaining
#so we dont need to write one here
'''

'''
Given an array of nums of n integers, are there elements a,b,c in nums
such that a+b+c=0. Find all unique triplets in the array which gives the
sum of zero.

Example: [-1,0,1,2,-1,-4]

1. approach 1:
   Brute Force: check all combinations which equal to zero. O(n³) complexity
   Sapce Complexity is O(n)

2. But we can do better, for sure:
   We can consider a two sum approach first:
   Build a dictionary in python --> hashmap here: for each element we get
   the complement: search for the complement: if complement in list and not equal
   to the same one then we have it.

   We extend this approach to three sum:
   if the complement
'''
