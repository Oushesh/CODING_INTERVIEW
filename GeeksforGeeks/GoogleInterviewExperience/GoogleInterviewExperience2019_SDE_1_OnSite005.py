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


weight_right = sum(left_part)
weight_left = sum(right_part)

"we keep on moving as long as the weight difference is
being minimised"

1,2,4,7,3,6 |9|

subaraay_count : keep track
max = 9
3, 9
|7| |7|, |3,6| |9|
14,15


right = 9
left = 1

At each step we have
1,2,4,7,3,6,9

curr_diff = 8
lowest_diff = curr_diff = 8

9-1 = 8
So we 2 choices:
i) 9+6 = 15 15-1=14
ii) 9-2=7

|1,2|,4,7,3,6,|9|
9-3=6 --> current
15-3=12

split = 2, continue looping until split == given_number
9-7=2 --> |1,2,4|,|7| ,|3,6|,|9|

'''

#TODO: COmplete by tomorrow.


#TODO: implement also a C++ version of the code.
