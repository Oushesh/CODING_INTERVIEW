'''
Reference: https://tutorialspoint.dev/algorithm/pattern-searching-algorithms/aho-corasick-algorithm-pattern-searching
'''
'''
The algorithm consists of the following:

1. Preprocessing: Build an automaton of all words in array

    Automaton has the following 3 steps:
    i) GoTo: This function simply follows edges of Trie of all
              words in arr. Represented as g[][]: next state for current state
              and character --> x dim (state), dim(character)
    ii) Failure: This function stores all edges that are followed when
        current character doesn't have edge in Trie. (query next state and see if result is empty)
        It is represented as 1D Array f[] where we store next state for current state.

    iii) Output: stores  indices of all words that end at current state.
         It is represented as 1D array O[]


2. Traverse the given text over built automaton to find all matching words.
'''

'''
Preprocessing for Arr = {'he','she','his','hers'}

The trie is done via the preprocessing
'''
from collections import deque
#Builds the string matching machine
#arr - array of words
#returns the number of states that the built machine has
#states are numbered
def buildingMatchingMachine(arr,k,out,g,f,states):
    #Construct values for goto function: i.e.
    #fill g[][]--> Building Trie
    MAXC = 26
    for i in range(k):
        word = arr[i]
        currentState = 0

    # Insert all characters of current word in arr
    for j in range(len(word)):
        ch = ord(word[j])-ord('a') # Get ascii correspondence value of the current character

        #allocate a new node (create a new state) if a
        #node for ch doesn't exist.

        if g[currentState][ch]==-1:
            states +=1
            g[currentState][ch]=states
        currentState = g[currentState][ch]

    #Add current word in output function
    out[currentState] |= (1 << i)


    #For all characters which don't have an edge from
    #root (or state 0) in Trie, add a goto edge to state
    #0 itself

    for ch in range(MAXC):
        if g[0][ch]==-1:
            g[0][ch] = 0


    #now let's build the failure function
    q = deque()

    #Iterate over possible combination
    for ch in range(MAXC):
        #All nodes of depth 1 have failure function value
        #0. For example, here when we move to 0 from states 1 and 3.
        if not g[0][ch]==0:
            f[g[0][ch]] = 0
            q.append(g[0][ch])

    #Now queue has states 1 and 3
    while q:
        #pop the front node
        state = q.pop()


        #For the removed state, find failure function
        #for all those characters for which goto
        #function is not defined

        for ch in range(MAXC):
            #if goto Function is not defined for ch and state
            if not g[state][ch]==-1:
                #Find failure state of removed state
                failure = f[state]

                #Find the deepest node labelled
                #by proper suffix from root to current state
                while (g[failure][ch]==-1):
                    failure = f[failure]

                failure = g[failure][ch]
                f[g[state][ch]] = failure

                #Merge output values:
                out[g[state][ch]] |= out[failure]

                #Insert the next level node of Trie in Queue
                q.append(g[state][ch])
    return states


#Now its time to find find the next state
#Returns the next state the machine will transition to using
#goto and failure functions.
#currentState - The current state of the machine. Must be
#between 0 and the len(states)-1, inclusive.
#nextInput - The next character that enters into
#the machine.

def findNextState(currentState, nextInput,g,f):
    answer = currentState
    #convert char to asci to be used as indexing

    ch = ord(nextInput) - ord('a')

    #if we goto is undefined (-1): means there is
    #a failure, dotted line: use failure function
    while (g[answer][ch]==-1):
        answer = f[answer]
    return g[answer][ch]

#This function finds all occurrences of all array words
#in text
def searchWords(arr,k,text):
    '''
    Initialise the matrices
    '''
    MAXS = 500
    MAXC = 26
    #output is implemented as out:
    out = [0 for i in range(MAXS)]

    #Failure implemented as f
    f = [-1 for i in range(MAXS)]

    #Goto Function (TRIE) implemented as g
    g = [[-1 for i in range(MAXS)] for j in range(MAXC)]

    #State
    states = 1

    #Preprocess patterns
    #Build Machine with goto, failure, output functions
    buildingMatchingMachine(arr,k,out,g,f,states)

    #Initialise current state
    currentState = 0

    #Traverse the text through the built machine
    #to fill all occurrences of words in arr.

    for i in range(len(text)):

        currentState = findNextState(currentState,text[i],g,f)

        #if no match found, move to next state
        if not out[currentState]:
            continue
        #Match found, print all matching words of arr
        #using output function
        for j in range(k):
            if out[currentState] and (1<<j):
                print ('output current state', out[currentState],'and', 1<<j)
                print ('Word',arr[j],'appears from',i-len(arr[j])+1,'to',i)
    return None

if __name__ == '__main__':
    arr = ['he','she','hers','his']
    text = 'ahishers'
    k = len(arr) #number of elements
    searchWords(arr,k,text)
