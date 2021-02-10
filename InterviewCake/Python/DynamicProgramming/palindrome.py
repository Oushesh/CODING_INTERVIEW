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

1) 2 pointers (left, right).
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


Space Complexity: O(n) --> output which a list and if the n! --> if the question says only true or false: O(1)
Time Complexity: O(n)

2) Second Approach is will also have the same time and space Complexity of O(n)
   We have 2 pointers mid_left, mid_right starting from the middle.

   In this case we move left and right simultanueously if the mid one is palindrome.
   append(output) as well. 'anna'--> 'nn', 'anna'
                           'bnnaa' --> 'nn',

   This one is more complicated.

   if true==palindrome(bigString) --> true==palindrome(substring), this reduces
   a lot complexity problem.

'''
class Words():
    def palindrome(self,string):
        return string==string[::-1]
    def check(self,string):
        output = []
        left = 0
        right = len(string)

        #The biggest value of a coder is to fix his own bugs in thinking
        while (right>left):
            if (self.palindrome(string[left:right])):
                output.append(string[left:right])
                left+=1
                right-=1
            if not self.palindrome(string[left:right]):
                left+=1
            if not self.palindrome(string[left:right]):
                right-=1
        return output

if __name__ == "__main__":
    string = "anna"
    given_words = Words()
    print ('The palindromes from this string are:', given_words.check(string))
