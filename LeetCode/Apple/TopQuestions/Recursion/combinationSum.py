'''
Given a set of candidate numbers (candidates) (without duplicates) and
a target number (target), find all unique combinations in
candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates
unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,2,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
'''
Let's use Dynamic Programming:
#Let's assume we have 2 indices i,j
#i=0,j=i+1
#As I move along the array I have 2 choices, I either
#add the new number if total < target or I discard it:
Example:
'''
