##
  Merge Sort

  One of the basic examples is divide-and-conquer
  algorithm is the merge sort algorithm. Merge sort
  is an efficient and general-purpose sorting algorithm.


###
   Intuition:
   There are 2 approaches to implement the merge sort
   algorithm: top down or bottom up.

   Let's talk about top down first:

   The merge sort algorithm can be divide into 3 steps,
   like all divide-and-conquer algorithms.

# 1. Divide the unsorted list into several sublists. (Divide)
# 2. Sort each of the sublists recursively. (Conquer)
# 3. Merge the sorted sublists to produce new sorted list. (Combine)


      |1|5|3|2|8|7|6|4|

   |1|5|3|2|      |8|7|6|4|

  |1|5|    |3|2|   |8|7|   |6|4|

|1|  |5| |3|  |2| |8|  |7| |6| |4|

##
  Step 3: Merge
 |1|5|   |2|3|   |7|8|   |4|6|

|1|2|3|5|       |4|6|7|8|

   |1|2|3|4|5|6|7|8|
