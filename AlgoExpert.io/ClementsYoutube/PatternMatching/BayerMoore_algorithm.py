'''
Reference: https://www.youtube.com/watch?v=PHXAOKQk2dw,
https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/?ref=rp


Best Reference: https://www.coursera.org/lecture/algorithms-part2/boyer-moore-CYxOT


In the field of pattern matching: we have
Naive Pattern matching of the order O(n²)

len(Text): n
len(pattern): m

The Bayer Moore_Algorithm attempts to solve
the problem in linear time in average case

Its based on the combination of 2 approaches.
1) Bad Character Heuristic
2) Good Suffix Heuristic

1. Preprocess the pattern and construct the bad match table.
   Value = length(pattern) - index - 1
'''

'''
2. Loop over the main(text) from last elemennt of pattern until
   end of text.
   len(text)=n
   len(pattern)=m,
   #check
   assert(m>n)
   count = 0
   for idx in range(n,m):
       idy = n
       if not text[idx]==pattern[idy]:
            bad_char = pattern[idy]
            shift = bad_match[bad_char] --> retrieve the query number
            idx = idx+shift
       while (text[idx]==pattern[idy]):
           count +=1
           idy-=1
           idx-=1
           return True if count==m
'''
class BoyerMoore():
    '''
    Encaluslates pattern and associated Boyer-Moore preprocessing
    '''
    def __init__(self,p,alphabet='ACGT'):
        self.p = p
        self.alphabet = alphabet

        #Create map from alphabet characters to integers.
        #Computationally cheaper--> assign the same
        self.map = {}
        for i in range(len(self.alphabet)):
            self.map[self.alphabet[i]]=i

        self.bad_char = dense_bad_char_tab(p,self.map)

        # Create good suffix rule table
        # Create g



def bad_match(pattern):
    bad_match = {}
    for i in range(len(pattern)):
        bad_match[char]=len(pattern)-i-1
    '''
    last letter of the bad_match: len(pattern) if not already defined
    '''
    bad_match['*']=len(pattern)
    return bad_match

def find_pattern(text,pattern):
    m=len(text)-1
    n=len(pattern)-1
    assert(m>n)
    shift=0
    for i in range(n,m-n):
        #reverse loop to check
        for j in range(n,0,-1):
            while (text[]==pattern[j]):

    return idx

##############################################################

#Reference: https://www.coursera.org/lecture/algorithms-part2/boyer-moore-CYxOT

class BoyerMoore():





if __name__ == "__main__":
    text = 'trusthardtoothbrushes'
    pattern = 'tooth'
    print ('Bad Match Table:',bd_match(patter))
