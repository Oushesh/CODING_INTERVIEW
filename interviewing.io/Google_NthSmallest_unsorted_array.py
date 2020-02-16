'''
# 1 6 3 9 2 5
#1st smallest = 1
#2nd smallest = 2
#nth order statistic = nth smallest in the set

First Approach: sort the list of length n -> log(n)
                then query n-1 element in list. assuming we
                len(list) > n
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
if __name__ == '__main__':
    number = [3,2,5,6]
    n      = 2 #second smallests
    output = Solution()
    print (output.smallest(number,n))
