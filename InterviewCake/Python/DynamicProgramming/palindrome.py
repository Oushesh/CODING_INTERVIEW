'''
Author: Oushesh

This code is here to check whether a piece of string or array
is a palindrome.

Example: "anna" --> reversed --> "anna"

in python this is super simple-> just reverse the string and check.
it will work. what if instead we would have to find all the possible
palindrome substring within the given big string.


For example here: 'nn' is a palindrome, 'anna' is also a palindrome.
(its continuous)

What about this case? --> 'banna'


2 Approaches I can think of:

1. 2 pointers (left, right).
left = 0, right = len(string)
while (left<=right):
    check_palindrome(substring)
    left+=1
    if not check_palindrome:
        right-=1
        check_palindrome

'''
