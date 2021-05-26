'''
Alien Dictionary Problem:

There is a new alien language
which uses latin alphabet. (I can read it, 26 alphabets)
You receive a list of non-empty words from dictionary.
--> words sorted lexicographically.
Find the order of letters

'wrt'-> w>r>t
'wrf' -> w>r>f
'er' -> e>r
'ett' -> e>t
'rftt' -> r>f>t

wertf, werft

w --- > r ---> t
          ---> f --> t

e ---> r
  ---> t
  --->

Topological search:
Build a matrix for each word and with each character


1. TODO: topological sort here.
'''
from collections import defaultdict, deque

def topoological_search():
    in_degree = {ch:0 for word in words for ch in word}

    for word in words:


if __name__ == '__main__':
    words = ['wrt','wrf','er','ett','rftt']
    print ()
