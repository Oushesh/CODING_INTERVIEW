'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/?ref=rp

Round 3: On site ( DS & Algo) ( 1 hr )

She asked for binary search functionality which tells number exists in array or not.
Generally we find mid-element through (low + high) / 2 so she asked to change that
and use random function to decide mid.

Binary search is performed on sorted array but here unsorted array is given.

Two modifications are performed on binary search logic.

1) instead of sorted array, unsorted array has been given

2) Mid element is decided based on random function. Now we have to find out
numbers from given array for which this function gives true result.

Hint: Function will return true for value x, if all numbers on left side of x
are small and all number on  the right side of x are greater.

Example: [ 4, 3, 1, 5, 7, 6, 10]

Ans: 5, 10

if sorted: [1,3,4,5,6,7,10] --> real_mid is 5, max is 10

Pseudocode:
If we use random how do we decide mid? Check the hint



Binary Search Tree Condition: left<mid<right


Instead of randomising the numbers: we randomise the index(0,len(numbers))
visited = set()
visited.add((element))
if rand not in visited:
    #initialise it first
    output = []
    mid =
    while query(left)<rand<query(right):
        if rand not in visited:
            visited.add(rand)
            query(left) --> i-1
            query(right) --> i+1
    output.append(swap(a,b)) append



Time Complexity: O(n)
Space Complexity: O(n)
'''

from random import random

class RandomBinarySearch():
    def __init__(self,numbers):

    def rand(self,interval,numbers):
        '''
        interval: int
        return idx numbers from 0 to that number-1
        '''
        return ramdom.randint(0,len(numbers))

    def swap(self,a,b):
        a,b = b,a
        return a,b

    def sort(self,numbers):
        '''
        initialise the variables first
        '''
        mid = None
        left = None
        right = None
        visited = []
        max = None

        '''
        Continue to generate random indices
        until we did not have all the indices here
        '''
        while not len(visited)==len(numbers):
            rand=self.rand(interval,numbers)
            if rand not in visited:
                while numbers[left]<numbers[rand]<numbers[right]:
                    if rand is None:
                        mid = rand
                        left = rand-1
                        right = rand+1
                        visited.append(mid)
                        visited.append(left)
                        visited.append(right)
                    else:
                        #rand, left,right is already has a none value
                        #ensure: left<rand< right
                        if not numbers[left]<numbers[rand]:
                            left,mid = swap(left,rand) #just swap the index
                        if not numbers[rand]<numbers[right]:
                            mid,right = swap(mid,right)
                    rand=mid
        return mid,max


if __name__ == "__main__":
    numbers = [4,3,1,5,7,6,10]

    print ('The max is ',RandomBinarySearch())
    print ('The mid is',RandomBinarySearch())


###TODO: debug and crosscheck
