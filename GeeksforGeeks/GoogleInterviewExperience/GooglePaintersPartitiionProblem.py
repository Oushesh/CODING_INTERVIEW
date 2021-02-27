'''
We have to print n boards of length {A1,A2,...An}.
There are k painters available and each takes 1 unit of time
to paint 1 unit of board. --> 1 unit of Board Length = 1 unit of time.

The problem is to find the minimum time to get this job done under the
constraints that any painter will only paint continuous sections of
boards, say board {2,3,4} or only board {1} or nothing but board {2,4,5}.

EXAMPLE:

It is obvious that the strategy of dividing the boards into k equal
partitions won't work for all the cases. We can observe that the problem
can be broken down into: Given an array A of non-negative integers and
a positive k, we have to divide A into k of fewer partitions such that
the maximum sum of the elements in a partition, overall partitions is
minimized.

For example:
 k = 2, A = {10, 20, 30, 40}
if partition = 1:
so time=100 max_sum(A)=100

if partition = 2:
    10, 20,30,40 max(90)
    10,20,30,  40 max(60)

min(100,90,70,60)=60


Lets say T(n,k)
T(1,1)
T(1,2)
T(1,3)
General Formula:  min(max(T(i,Ki-1),sum(A1,--An)))

n = length of the array
k: number of constraints or divisions.
         T(4,3)
          /  \

'''

#Good problem: To complete.
