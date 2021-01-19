#https://www.geeksforgeeks.org/google-interview-experience-on-site-for-sde/

'''
Round 4: This was a classical dynamic programming problem of
palindrome partitioning.

Input: str = "geek"
OUtput: 2

Input: Str = "aaaa"
Ouput: 0

Input: str = "abcde"
Output: 4

Input: str = "abbac"
Output: 1


Dynamic Programming Problem:

Lets take the example given:
""

geek, break_count = 0
i=len(str)+1/2 if odd, else len(str)/2, j=next to i

while (i>0 and j<len(str)) --> just to make sure the indices stay within boundaries
if s[i]==s[j]:

    i=i-1
    j=j+1
else:
    break_count

et voila!!

Now lets walk the interviewer through when we dont find a match at the beginning.
We use for this a dynamic programming approach.
Example:

'abcde'
i = 2 @c, j = 3 @d, cd not a palindrome,
breakcount = 1, split --> abc, de --> run recursive function
check on abc, and de. return check_palindrome (abc, de)
'''


class Palindrome:
    #Recursive solution
    def check_string(self,strings,breakcount=0):
        for string in strings:
            '''
            Initialisation, i,j,breakcount
            '''
            if len(string)==2:
                if string==string[::-1]:
                    substring.pop(string) #remove the string to avoid gettting infinite loop
                    return None
            else:
                if len(string)%2==1:
                    i = len(string)+1/2 -1 #index i
                    j=i+1                  #index j
                else:
                    i=len(string)/2 -1  #index i
                    j = i+1         #index j

                '''
                initialisation ends here
                '''
                #stop the indices going out of bounds
                while (i>0 and j<len(string)):
                    #Check palindrome condition here: --> s==s[::-1]
                    sub = string[i:j]
                    if sub==sub[::-1]:
                        #Substring is a palindrome, then we move the i to left, j to right
                        i=i-1
                        j=j+1
                    else:
                        breakcount+=1
                        substrings = [string[0:i],string[j:len(string)]]
                        self.check_string(substrings,breakcount)
        return breakcount

if __name__ == "__main__":
    string = 'geek'
    current_palindrome = Palindrome()
    current_palindrome.check_string(string)


#TODO: Todebug and to check the code subtulties
