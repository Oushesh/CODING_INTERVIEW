'''
Interviewing.io #Reference:
https://interviewing.io/recordings/Java-Google-2/
'''

'''
1st approach: Sort everything then query the 3rd element
Time Complexity: O(nlogn)

Can we do better? Yes. Lets try a dynamic approach,
as we iterate we sort. In the end we will traverse
the list only once, So time complexity has to be n.
'''

class Integers:
    '''
    nlogn Time Complexity
    '''
    def third_smallest_sort_approach(self,numbers):
        assert (len(numbers)>0)
        return sorted(numbers)[2]

    def third_smallest_linear_approach(self,numbers):
        assert (len(numbers)>0)
        return None
        '''
        smallest =
        second_smallest =
        third_smallest =

        return third_smallest
        '''

    '''
    2 pointers approach. Declare 1 pointer on left, one on right
    O(logn)
    '''
    def third_smallest_finest_approach(self,numbers):
        '''
        This approach is the finest since
        we will dynamically sort the array.
        '''
        left  = 1 #index of first number
        right = len(numbers)-1 #index of last number
        while (left < right):
            if numbers[left-1] > numbers[left]:
                #perform swap here
                numbers[left-1],numbers[left] = numbers[left], numbers[left-1]
                left +=1 #move  left to the right
            if numbers[right] < numbers[right-1]:
                numbers[right], numbers[right-1] = numbers[right-1], numbers[right]
                right -=1
        return numbers[2]

class Solution_nth():
    def smallest_n(self,number,n):
        left = 0
        right = len(number)-1
        current = 1
        '''
        loop over the list only once
        only under the condition that current <=right
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
        return number[n]

if __name__ == "__main__":
    numbers = [1,4,3,8,2]
    current_Integers = Integers()
    print ('The third smallest number is:',current_Integers.third_smallest_sort_approach(numbers))
    print ('The third smallest number based on simultaneous sorting is:',current_Integers.third_smallest_finest_approach(numbers))
    generic_solution = Solution_nth()
    n = 3
    print ('The third smallest number based on generic n approach is:',generic_solution.smallest_n(numbers,3))
