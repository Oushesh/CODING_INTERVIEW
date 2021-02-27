'''
Ref: https://www.geeksforgeeks.org/allocate-minimum-number-pages/

Given number of pages in n different books and m students.
The books are arranged in ascending order of number of pages.
Every student is assigned to read some consecutive books. The
task is to assign books in such a way that the maximum number
of pages assigned to a student is minimum.

n - books [1,2,...n]
m - students

Way 1: Dynamic Programming Build a precomputed matrix
Way 2: BInary Search.

If k=2 we can do binary search. -->
everything that lower than the mid can be on the left

i) mid,
ii) left,
iii) right,
'''
