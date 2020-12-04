'''
Reference: https://www.youtube.com/watch?v=PHXAOKQk2dw,
https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/?ref=rp

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
   Value = length - index - 1
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

def find_pattern(text,pattern):

    return idx


def bad_match(pattern):
    bad_match = {}
    for i in range(len(pattern)):
        bad_match[char]=len(pattern)-i-1
    '''
    last letter of the bad_match: len(pattern) if not already defined
    '''
    bad_match['*']=len(pattern)
    return bad_match


if __name__ == "__main__":
    text = 'trusthardtoothbrushes'
    pattern = 'tooth'

    print ('Bad Match Table:',bd_match(patter))
