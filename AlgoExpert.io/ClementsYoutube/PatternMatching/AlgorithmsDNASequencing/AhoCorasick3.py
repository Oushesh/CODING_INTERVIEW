'''
Self implementation: https://www.toptal.com/algorithms/aho-corasick-algorithm
'''

#each vertex in the trie will store the following information

class Vertex:
    def __init__:
        self.Children = defaultdict()
        self.leaf = False
        self.parent = -1
        self.SuffixLink = -1
        self.WordID = -1
        self.EndWordLink = -1


    #Links to the child vertices in the trie:
    #Key: A single character
    #Value: ID of vertex

#Next, define a list of vertices and initialize
#the root node of the Trie.

class Aho:
    def __init__:
        #Trie is a list of children which is a defaultdict
        self.Trie = [] #empty list, just append vertex here
        self.WordsLength = None
        self.size = 0
        self.root = 0

        Trie = list(Vertex)
        Trie = self.Trie

        WordsLength = []
        WordsLength = self.WordsLength

        size+=1
        size=self.size
        root = self.root

    #Then we add all patterns to the trie. For this, we need a
    #method to add words to the trie.
    def addstring(self,s,wordID):
        curVertex = root
        #iterate over the string's characters
        for i in range(len(s)):
            c = s[i]
            #Checking if a vertex with this edge exists
            #in the trie
            if not c in Trie[currVertex].Children.keys():
                Trie.append(Vertex)
                Trie[size].SuffixLink = -1

                Trie[size].Parent = c
                Trie[curVertex].Children[c] = size
                size+=1

        curVertex = Trie[curVertex].Children[c] #Move the new vertex in the trie


        #Mark the end of the word and store its ID
        Trie[curVertex].Leaf = True
        Trie[curVertex].WordID = WordID
        WordsLength.append(len(s))

#Next we calculate all sufix Links and dictionary entry links.



if __name__ == "__main__":
    words = ['bar','ara','bara','barbara']
