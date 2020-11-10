#Reference: 'interviewing.io'
#TUM Exercise on search

'''
WHat to say to the interviewer?
1. This is a search problem with start node: dog
   and end node: hat. Thus we need to build a graph
   and traverse it.

2. How do we decide whether 2 words in the dictionary
   are neighbours or not? Well if the 2 words are
   in the dictionary and they differ by 1 letter
   then we add them to graph and as the neighbours
   of the others.

3. Clear this with the interviewer. What are the
   constraints? Example: both start and end word
   have to be inside the dictionary.

4. Tell about the space and time complexity of the
   algorithm. O(V+E) time complexity.
   Worst Case of depth search to be written:
   Depth: D, Branching Factor: a
   O(D^a)
Now algorithmic Thinking:

In Python we use either recursive function or
stack for DFS.


How do we define the graph?
graph = {'dog':set(['dot','hot','hat'])}
'''

class Word():
    #2 ways of doing difference
    def difference(self,word1,word2):
        '''
        Both words need to be of the same length
        Return true if differ by 1 letter else False
        '''
        assert(len(word1)==len(word2))
        differences = 0
        for i in range(len(word1)):
            if not word1[i]==word2[i]:
                differences+=1
            if differences > 1:
                return False
        return True

    def difference_set_method(self,word1,word2):
        '''
        Use set method and perform intersection
        with set operation
        '''
        assert(len(word1)==len(word2)) #if not the its an error
        if len(set(word1)-set(word2))==1:
            return True
        return False

    def build_graph(self,dictionary):
        '''
        Expected Data type:
        graph = {'dog':set([]),
        'cat':set([]),
        'hot':set([]),
        'eat':set([]),
        'dug':set([]),
        'dig:set([])'}
        '''
        graph = {words:set() for words in dictionary}
        #We do not want to have a bidirectional graph. We dont add twice
        track = set()
        for i  in range(len(dictionary)-1):
            for j in range(1,len(dictionary)):
                #Call the function differby1 letter here: if True then add it as neighbour
                if self.difference(dictionary[i],dictionary[j]):

                    graph[dictionary[i]].add(dictionary[j])
        return graph

    '''
    Pass Graph here and perform dfs
    '''
    def dfs(self,graph,start,end,visited):
        if visited is None:
            visited = set ()
        visited.add(start)
        #Loop over the graph
        #over the children and not
        #in visited
        for neighbours in graph[start]-visited:
            self.dfs(graph,neighbours,end,visited)
        return visited
        '''
            else:
                print ('Goal is reached')
                return True
        return False
        '''

    def main(self,dictionary,start,end):
        '''
        1. Call Function Build graph.
        2. Then perform dfs on graph and check
            if goal or end is met.
        3. If 2. returns true then, is_Transformable
           else not.
        '''
        word_graph = self.build_graph(dictionary)

        visited = None
        path = self.dfs(word_graph,start,end,visited)
        print ('path',path)
        '''
        if self.:
            return True
        return False
        '''

if __name__ == "__main__":
    dictionary = ['dog','cat','hot','hog','eat','dug','dig']
    '''
    example: start: 'dog', end: 'hat'
    #Path then is: 'dog'-> 'dot'-> 'hot'->'hat'
    Function should return true if a path is found
    else  false
    '''
    start = 'dog'
    end   = 'hat'
    graph = {}
    current_game = Word()

    print ('The given word is transformable:',current_game.main(dictionary,start,end))
