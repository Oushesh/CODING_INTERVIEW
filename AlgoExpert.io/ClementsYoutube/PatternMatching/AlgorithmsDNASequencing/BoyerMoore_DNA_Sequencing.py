'''
Algorithm for DNA Sequencing: https://www.cs.tufts.edu/comp/150GEN/classpages/BoyerMoore.html#:~:text=Good%20suffix%20rule%3A%20If%20t,of%20t%20as%20a%20suffix
'''

class BoyerMoore():
    def bad_character(self,pattern,text):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = len(pattern) -i -1
        return table

    '''
    Good suffix rule is broken into 3 parts:
    1.
    2. Find the smallest shift that matches a prefix of the pattern to a suffix of t in the text
    3. If there's no match, shift the pattern by n (len(p))
    '''
    #Case 1
    def longest_suffix(self,pattern,text,i,j):
        return shift

    #Case 2 prefifx, t of pattern against suffix  t in text
    #This function is only called when there is MISMATCH in
    #main function: search function described below
    def smallest_shift(self,pattern,text,i,j):
         if pattern[]==text[]:
             return None
        return shift

    #Case 3 No match
    def no_pattern(self,pattern,text,i,j):
        mismatch = False
        while (j>=0 and not pattern[i]==text[j]):
            i=-1
            j=-1
        if (j==0):
            mismatch = True
        return mismatch


    def good_suffix(self,pattern,text):
        if :
            shift = None
        elif:
            shift = None
        elif self.no_pattern[0]:
            shift = len(pattern)
        return table

    def search(self,pattern, text):
        m = len(text)-1
        n = len(pattern)-1
        assert(m>n)
        #index i loops over text, index j loops over pattern

        for i in range(n,m):
            while (j>=0 and j<=n):
                 #Call all 3
                 return None
        return None

if __name__ == "__main__":
    text = 'trusthardtoothbrushes'
    pattern = 'tooth'
    pattern_matching = BoyerMoore()
    print ('The bad character table is:',pattern_matching.bad_character(pattern,text))
    print ('The shift based on good suffix rule is:',pattern_matching.good_suffix(pattern,text))
    print ('The search for the pattern in the text results in:',pattern_matching.search(pattern,text))
