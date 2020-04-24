'''
Longest Palindrome of a string:
'''

'''
Example:
Longest Palindrome
Find the length of the longest substring in the given string s that is the same
in reverse.

As an example, if the input was “I like racecars that go fast”, the substring
(racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.
'''

class Palindrome:
    def longest_palindrome_length(self,s):
        '''
        Palindrome key idea is that the string
        reversed equals the same string.
        '''
        print ([i for i in range(len(s),0,-1)])
        #print ([j for j in range(len(s)-i+1)])

        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                sub = s[j:j+i]
                if sub == sub[::-1]:
                    return i
        return 0

'''
This one is approach I did on Leetcode the first time.
A bit nasty.
'''

class Solution(object):
    def longestPalindrome(self, s):
        largestPalindrome = ""
        for i in range(len(s)):
            palindromeOdd = self.largestPalindromeAtIndex(s, i, i)
            palindromeEven = self.largestPalindromeAtIndex(s, i, i + 1)
            largerPalindrome = palindromeOdd if len(palindromeOdd) > len(palindromeEven) else palindromeEven
            largestPalindrome = largestPalindrome if len(largestPalindrome) >= len(largerPalindrome) else largerPalindrome
        return largestPalindrome

    def largestPalindromeAtIndex(self, s, left, right):
        leftIndex = 0
        rightIndex = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftIndex = left
                rightIndex = right
            else:
                break
            left -= 1
            right += 1
        return s[leftIndex:rightIndex+1]

'''
Test Cases:
"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
'''

if __name__ == "__main__":
    s = 'zzbaabcd'
    current_Plandrome = Palindrome()
    print (current_Plandrome.longest_palindrome_length(s))

    current_Solution = Solution()
    print ('Nasty solution on leetcode first time',current_Solution.longestPalindrome(s))
