'''
TODO: Ref: https://www.youtube.com/watch?v=a__WNOhL2q4&t=402s
#TO FINALISE
'''

'''
Problem Statement: Given a non-empty string s and a dictionary wordDict
containing a list of non-empty words, determine if s can be segmented into
a space-separated sequence of 1 or more dictionary words.
Lets say we have here
'''


'''
Example:
str = 'facebook'
set = ['face', 'book', 'facebook']

Algorithmic Thinking. --> Dynamic Programming problem.
why? facebook can be split into face and book and both of them can be
in the dictionary. In this case they are.

How to do dynamic programming? -->  Declare array: explored = [0 for i in str]
start_idx
current_idx
Looping and each time we check if str[start_idx:current_idx] in dict if a in b:
found.

The question says 1 or more. So Dynamic Programming needed:
Then comes the recursive thinking: The mathematical rule is the following:
each element can be split.


1. start_idx = 0
2. current_idx = 1
3. Combine the words and then check the resultant:
4. This allows to reduce the time complexity from O(n²) to O(n)
5. Check face --> True: sart_idx @ b from then on you continue looping:
    b:k --> book is in it. Then combine the strings and recheck: face+book
    face + book : Time Complexity Python: O(1) Chck of dictionary is constant.
6. Space Complexity: O(n) to save string, now becasue python has immutable string
    for facebook we have O(a+b) where a+b=n --> O(n) --> O(n²)
    In worst case we have:
    n+n-1
    n+n-1+n-2
    n+n-1+n-2+n-3
    n+n-1+n-2+n-3+n-4
    n+n-1+n-2+n-3+n-4+......1
    Space Complexity can become really high here: O(n^n)

    The sum of all the series will repeat n-1 times.
'''


'''
For example: 'facebook'
'''
class Solution:
    def recursive_check(string, list):
        
        return None




if __name__ == "__main__":
    string = 'facebook'
    list   = ['face','book','facebook']
    splitter = Solution.
