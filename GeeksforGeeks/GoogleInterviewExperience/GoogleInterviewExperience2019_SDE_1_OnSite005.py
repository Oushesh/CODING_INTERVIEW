'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/?ref=rp

Round 5: On site ( DS & Algo) ( 1 hr )
Similar to Round 4. There were n people each having some weight. You have to
divide them in k continuous group such that total weight difference between
groups will be minimised. You have to return difference between max and min
 weighted group.

Input: 1, 2, 4, 7, 3, 6, 9  N = 7, K = 4

Output: 2 (Divide it into 4 parts like [1, 2, 4] [7] [3, 6] [9] with weight
7, 7, 9, 9 respectively So answer will be 9 – 7

'''

'''
Input: 1, 2, 4, 7, 3, 6, 9

N = 7, K= 4 (number of parts is 4)
What does 7 have to do here?
For example: Divide such that weight is minimised --> sum of subarrays minimised
Output = diff(max,min)*weighted group


weight_right
weight_left

we keep on moving as long as the weight difference is
being minimised:

1,2,4,7,3,6 |9|

max = 9
3, 9
7, 9
14,15
'''
