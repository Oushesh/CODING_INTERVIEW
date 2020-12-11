'''
Reference:
https://medium.com/100-days-of-algorithms/day-34-aho-corasick-4b9f439d4712
'''

'''
Build the automaton
'''

from collections import deque, defaultdict
from itertools import count

def AhoCorasick():
    G = defaultdict(count(1).__next__)  # transitions
    W = defaultdict(set)                # alphabet
    F = defaultdict(lambda: 0)          # fallbacks
    O = defaultdict(set)                # outputs

    # automaton
    return G, W, F, O

def add_word(word, G, W, F, O):
    state = 0
    # add transitions between states
    for w in word:
        W[state].add(w)
        state = G[state, w]
    # add output
    O[state].add(word)



def build_fsa(G, W, F, O):
    # initial states
    queue = deque(G[0, w] for w in W[0])

    while queue:
        state = queue.popleft()

        # for each letter in alphabet
        for w in W[state]:
            # find fallback state
            t = F[state]
            while t and (t, w) not in G:
                t = F[t]

            # for next state define its fallback and output
            s = G[state, w]
            F[s] = G[t, w] if (t, w) in G else 0
            O[s] |= O[F[s]]

            queue.append(s)
    return G,W,F,O

def search(text, G, W, F, O):
    state = 0
    for i, t in enumerate(text):
        # fallback
        while state and (state, t) not in G:
            state = F[state]

        # transition
        state = G[state, t] if (state, t) in G else 0

        # output
        if O[state]:
            print(O[state])

if __name__ == "__main__":
    words = ['bar','ara','bara','barbara']
    algorithm = AhoCorasick()
    '''
    Normally, I dont use the * but signifies that you
    '''
    #build_Trie(words,*algorithm)
    #Build the automaton with all the args output
    #from the build_trie
    add_word('bar', *algorithm)
    add_word('ara', *algorithm)
    add_word('bara', *algorithm)
    add_word('barbara', *algorithm)
    build_fsa(*algorithm)

    print (build_fsa(*algorithm))
    print (search('barbarian barbara said: barabum', *algorithm))
