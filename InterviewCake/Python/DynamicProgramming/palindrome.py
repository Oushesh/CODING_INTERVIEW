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
    while  check_palindrome(substring):
        output.append(substring)
        left+=1
        right-=1
    #If not palindrome then test either by moving left or right individually at one time
    if not check_palindrome:
        left+=1
    if not checkpalindrome(substring):
        right-=1
'''

class String():
    def palindrome
    def check(self,string):
        output = []
        left = 0
        right = len(string)

        #The biggest value of a coder is to fix his own bugs in thinking
        while (right>left):
            if (self.check(string[left:right])):
                output.append(string[left:right])
                left+=1
                right-=1
            if not self.check(string[left:right]):
                left+=1
            if not self.check(string[left:right]):
                right-=1
        return output


if __name__ == "__main__":
    string = "anna"
    current_palindrome = Palindrome()
    print ('The palindromes from this string are:', current_palindrome.check(string))
