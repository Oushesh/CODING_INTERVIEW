'''
Reference: https://www.tutorialspoint.com/Aho-Corasick-Algorithm
Aho-Corasick Algorithm Implementation
'''
#Build Finite State Automaton and perform a Breadth First Search on it.
#ord() in python to just to get a nunique mapping of the string as index

from collections import deque

def buildTree(arr, size,MAXS, MAXC,gotoMat,fail,output,state):

    #Make trie structure for all pattern in array
    for i in range(size):
        word = arr[i]
        presentState = 0
        #All pattern is added

    #pattern added, pattern
    for j in range(len(word)): #all pattern is added
        ch = ord(word[j]) - ord('a')

        #if the asci version of the character is not present:
        #ch is not present: make new node
        print ('word[j]',word[j])
        print ('ch',ch)
        print ('presentState',presentState)
        print ('gotoMat',len(gotoMat[0]))
        if (gotoMat[presentState][ch]==-1):
            state+=1 #update state
            gotoMat[presentState][ch] = state
            presentState = gotoMat[presentState][ch]

        #current word added in the output
        output[presentState] |= (1 << i)

    #if ch is not directly connected to root
    #ch ascii code for the problem
    for ch in range(MAXC):
        if gotoMat[0][ch]==-1:
            gotoMat[0][ch]  = 0

    #Just add the modified BFS code here:
    #Call the BFS traversal here:
    state = BFS_traversal(MAXC,gotoMat,fail,output)
    return state

# modified BFS_traversal function to accomodate the functionalities
# of AhoCorasick Algorithm
# Here tell the interviewer why you use: deque vs list
# deque.popleft() is faster than list.pop(0),
#because the deque has been optimized to do popleft()
#approximately in O(1), while list.pop(0) takes O(n) (see deque objects).

def BFS_traversal(MAXC,gotoMat,fail,output):
    q = deque([])

    #Node goes to previous state when it fails
    for ch in range(MAXC):
        if not gotoMat[0][ch]:
            fail[gotoMat[0][ch]] = 0
            q.append(gotoMat[0][ch])
            #print ('q')
    #Pop all the elements 1 by 1:
    while q:
        #remove front node
        state = q[0]
        q.popleft()

        for ch in range(MAXC):
            #if goto state is present
            if not gotoMat[state][ch] == -1:
                failure = fail[state]

                #Loop and find the deepest node with proper suffix
                while gotoMat[failure][ch] == -1:
                    failure = fail[failure]
                failure = gotoMat[failure][ch]
                fail[gotoMat[state][ch]] = failure

                #merge output values
                output[gotoMat[state][ch]] |= output[failure]
                #add next level node to the queue
                q.append(gotoMat[state][ch])
    return state


def getNextState(presentState, nextChar,gotoMat,fail):
    answer = presentState
    #Either get the ascii
    ch = ord(nextChar) - ord('a') #get the ascii of the character to
    while (gotoMat[answer][ch]==-1):
        answer = fail[answer]
    return gotoMat[answer][ch]

def patternSearch(arr,size,text):
    #Variables intialisation
    MAXS = 500
    MAXC = 26
    #initialise all elements of output to 0
    output  = [0 for i in range(MAXS)]
    fail    = [-1 for i in range(MAXS)]
    gotoMat = [[-1 for i in range(MAXS)] for j in range(MAXC)]
    state   = 1

    buildTree(arr,size,MAXS,MAXC,gotoMat,fail,output,state) #make the Trie structure
    presentState = 0 #make current state 0

    #Find all occurrences in the pattern
    for i in range(len(text)):
        presentState = getNextState(presentState,text[i],gotoMat,fail)
        #if no mastch found we continue
        if not output[presentState] == 0:
            return
        #matching found and print words
        for j in range(size):
            if (output[presentState] and (1 << j)): #(1==j)
                print ('Word', arr[j], 'location: ', i-len(arr[j]+1))
        return None

if __name__ == "__main__":
    arr = ['their', 'there', 'answer', 'any', 'bye']
    k = len(arr) #k--> number of elements
    text = 'isthereanyanswerokgoodbye'
    patternSearch(arr,k,text)
