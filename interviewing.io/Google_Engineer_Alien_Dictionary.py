'''
The following contains 2 interview sessions both termed
as Google Engineer: https://www.youtube.com/watch?v=Vy4RWh22ZPE&list=RDCMUCNc-Wa_ZNBAGzFkYbAHw9eg&index=3

The 2nd is here:
Google Engineer again: https://interviewing.io/recordings/C++-Google-21
2 questions here:

Perks of the second interview
1) Return a list of all paths to leaves in the tree
2) Given a lexicographically sorted list of words, return the order of
   the alphabet
'''

'''
Interview 1:
# Alphabet: b f g q
#
# bgg -> b-0 g-1 g-1
# fbq -> f-0 b-1 g-2 q-3
# fqf -> f-0 q-3 f-> violation
# ffq -> f-0 f-0 q-3
# gfg -> g-violation, f-0, g-3
#
# each time there is a violation we let it go.
# output: f->b->g


Algorithmic Thinking 1:
1. We assign the ranking in the form of a dictionay with value representing the rank
2. We update the rank by 1 for all members if something new precedes the one with rank 0
3. Collision check on each of them: if violation, set to another tracking variable to 1
4. Then if violation occurs then just neglect the new ranking and use the old one.
5. Thats it, return the dict in the end. The key of each element will determine the
   final ordering thus representing the dictionary aksed in this question.

AlgorithmiC Thinking 2:
1. We assign the ranking as children of the main nodes -> meaning: dictionary
   with every element: in the list:

initialise the dictionary: loop over the given list: build
an empty dict. graph= {i:[] for i in given_list}
2. If no violation of the data structure occurs: then add a second one:
   current_parent = b,
   bgg -> b:g, if the other nodes already contain children: then do not add.
   check for parent.

3. fbq -> check b viiolation. --> g:b,
   f precedes b and is the one: f:b, parent = f
   check (b,q) --> no violation. b:[g,q] check for g:q or q:g else: violation = set([g])

current_parent = f
q follows f.
4. fqf --> f:b, f:[b,q], check for (b,q) --> b:q or q:b, --> neglect q.
5. ffq: f is current_parent: f f is the same thing. q is violation. we neglect.
'''

'''
f -> b -> g -> q
0    1    2   -1
'''

'''

'''

class AlienDictionary():
    def ranking(self,alphabet,list):
        '''
        rank is a dictionary containing the rank. (rank, bool violation:-1 violated, 1 is not violated)
        '''
        current_parent = None
        rank = {i:[] for i in alphabet}
        for elements in list:
            for char in elements:
                #update the ranking
                if char in alphabet:
                    #check if alphabet is inside the dictionary
                    if len(rank[char])==0:
                        rank[char].append()
                else:
                    raise ValueError('Current char is not inside the dictionary')
        return rank
if __name__ == "__main__":
    alphabet = ['b','f','g','q']
    list = ['bgg','fbq','fqf','ffq','gfg']
    current_Dictionary = AlienDictionary()
    print ('The output ranking is:',current_Dictionary.ranking(alphabet,list))
