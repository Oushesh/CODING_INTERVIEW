'''
Ref: https://www.geeksforgeeks.org/google-interview-onsite-university-grad-2020/?ref=rp
'''
'''
Question:  Given an array of 2n elements you can choose n elements from either either (front or back)
           of the array such that the values obtained result in maximum sum.


Example: 1 3 100 25 20 4
OUtput:  100+4+20+25

From mathematics sum is a linear operator and so is max.

Approach 1:
So I can say max(sum(list) = sum(max(sublist))+sum(max(sublist)))
This makes it so simple. O(n) time complexity, iterative approach -> O(1) space complexity

Approach 2: Dynamic Programming, recursive approach


For the time being I choose approach 1 and execute.

Pseudo Code:

1 3 100 25 20 4.  left_sub = [1 3 100], right_sub = [25 20 4]
   --> Edge Case: what happens if the array is unbalanced?
                  If the len(array)%2 ==1 (odd) number
                  then what --> error either take 1 more to left or right. We choose right or just say error.

  max(left_sub,right_sub) --> 100, We further also assume we have choice by non-replacement (Communicate with interviewer
  strategy to win more points: we tak 100 without replacement)

  100 removed from list.

TODO: Redefine the Question properly.
'''

#TODO: To recheck the formulation of the question: https://www.geeksforgeeks.org/google-interview-onsite-university-grad-2020/?ref=rp
