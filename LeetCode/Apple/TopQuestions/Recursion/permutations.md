##
  Permutations
Given a collection of distinct integers, return all possible
permutations.

Example:
##
    Input: [1,2,3]
    Ouput:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

pivot = o
rest
swap(rest)
output = pivot + 2 possibilities of rest

make the next digit as pivot:
append pivot.
