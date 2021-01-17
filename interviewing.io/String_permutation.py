'''
Check if 2 strings are permutations of each other in python.

For example:
1)
str1 = "test"
str2 = "ttew"--> No

2) str1 = "geeksforgeeks"
   str2 = "forgeeksgeeks"

1. First approach is to sort the string and perform a direct string comparison
   sort in python: O(nlgn)--> and then do string comparison.
   space: O(1)--> we are not saving anything, just returning a boolean

   Can we do better? Lets say without sorting.
   Pairwise comparison is gonna cost O(n²) --> we can some more optimisations like

   I) If len(str) is not the same then just abrupt the process and return false.
   II) if we know the substring are a part of an english or french dictionary -->
       we can optimise this as well, where we actually search for the word from dictionary
       in our substring. Then we search only the subwords from the dictionary.

   III) Next step is to write it in C++.
'''

class String:
    def compare(self,s1,s2):
        return sorted(s1)==sorted(s2)




if __name__ == "__main__":
    s1 = "geekforgeeks"
    s2 = "forgeekgeeks"
    current_string = String()

    print ('Sting S1 & S2 are permutations of each other:',current_string.compare(s1,s2))
