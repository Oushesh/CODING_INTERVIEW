'''
Greedy Approach
'''
class Solution:
    def longestPalindrome(self,s:str)-> str:
        left = 0#0
        right = 2#2
        #save start index in different varaible
        #not update
        indices = []
        for i in range(1,len(s)-1):

            while left >= 0 and right < len(s):
                if s[left]==s[right]:
                    indices.append(left) #first left
                    left -=1
                    right +=1
            indices.append(right)
        return s[indices[0]:indices[-1]]

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

s = Solution()
print (s.longestPalindrome('babaabbaa'))


if __name__ == '__main__':
    #s = "ababa"
    s = "xaaabbaa"
    output = Solution()
    print ('The Longest Palindrome is:',output.longestPalindrome(s))
