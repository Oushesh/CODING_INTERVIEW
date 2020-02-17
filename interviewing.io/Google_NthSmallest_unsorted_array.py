'''
# 1 6 3 9 2 5
#1st smallest = 1
#2nd smallest = 2
#nth order statistic = nth smallest in the set

First Approach: sort the list of length n -> log(n)
                then query n-1 element in list. assuming we
                len(list) > n
O(n)log(n)
'''

class Solution():
    def smallest(self,number,n):
        return sorted(number)[:n]
'''
What if we did not have python method sorted?
Dynamic sorting: 2 pointers, one left, one right
Time complexity: n
Space Complexity: 1
'''
class Solution_brute_force():
    def smallest(self,number):
        min = number[0]
        for i in range(len(number)):
            if number[i] < min:
                min=number[i]
        return min

'''
Time Complexity: n
Space complexity: 1
'''
class Solution_Dynamic():
    def smallest(self,number):
        left  = 0
        right = len(number)-1
        current = 1
        min_left   = number[0]
        min_right  = number[right]
        while (current < right):
            if number[current] < min_left:
                min = number[current]
                current +=1
            if number[right] < number[right-1]:
                num = number[right-1]
                right -=1
        return min(min_left,min_right)

'''
How to improve the algorithm? to only log(n)
Steps: Start in the middle.
mid_pointer, left_pointer, right_pointer

'''
class Solution_nth():
    def swap(self,a,b):
        a,b = b,a #pythonic way of swapping
        return a,b
    def smallest_n(self,number,n):
        if len(number)%2==1:
            mid = int(len(number)/2)
        else:
            mid = int(len(number)+1/2)
        left = 0
        right = len(number)-1
        current = 1
        '''
        loop over the entire list only once
        '''
        while (current<=right):
            if number[current] < number[left]:
                number[left],number[current]= number[current], number[left]
                left +=1
            elif number[right] < number[current]:
                number[current],number[right]=number[right],number[current]
                right -=1
            else:
                current +=1
        return number

if __name__ == '__main__':
    number = [3,2,5,6]
    n      = 2 #second smallests
    output = Solution()
    print (output.smallest(number,n))

    output_nth = Solution_nth()
    print ('output_nth:',output_nth.smallest_n(number,n))
