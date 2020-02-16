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
        current = 0
        min_left   = number[0]
        min_right  = number[right]
        while (current < right):
            if number[current] < min:
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
loop:
    if right(mid) > current:
        right_pointer +=1
    else:
        swap(current,right)

    if left(mid) < current:
        left_pointer -=1
    else:
        swap(current,left)
'''
class Solution_nth():
    def smallest_n():
        return None

if __name__ == '__main__':
    number = [3,2,5,6]
    n      = 2 #second smallests
    output = Solution()
    print (output.smallest(number,n))
    output_Dynamic = Solution_Dynamic()
    print (Solution_Dynamic.smallest(number,n))
