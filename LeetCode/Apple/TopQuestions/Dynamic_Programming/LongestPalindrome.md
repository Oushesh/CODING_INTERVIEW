##
  Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

##
  Example 1:

  Input: "babad"
  Output: "bab"
  Note  : "aba" is also valid answer.


##
  Example 2:

  Input: "cbbd"
  Output : "bb"

##
  Definition:
  A palindrome is a string which reads the same in both directions. For example, SS = "aba" is a palindrome, SS = "abc" is not.  
  SS = "aba", SS_reversed= "aba"


##
  Solution 1: Obvious Brute Force.
  #Steps involve:
  #Reverse string O(n)
  #Compare string n and reversed(string(n)): O(n²)
  #Combined time complexity: O(n³)
  #Space Complexity: O(n²)

##
  Solution 2: What about Dynamic Programming?
  string s,
##
  Solution 3:
  Centering Technique.
  Get anchor there.
  Pointers i,j:
  Move pointer i to the left:
  i-=1 until i==0
  j+=1 until len(s)
  while:
    if s{[i]==s[j]}
  return s[i:j+1]
