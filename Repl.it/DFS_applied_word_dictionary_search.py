#Reference: 'interviewing.io'
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
        graph = {}
        return graph

    '''
    Pass Graph here and perform dfs
    '''
    def dfs(graph,start,end,visited=None):
        if start and end in graph:
            visited = set()
            if start not in visited:
                visited.add(start)

            #Loop over the graph
            #over the children and not
            #in visited
            for neighbours in graph[start]-visited:
                dfs(graph,neighbours,end,visited)
        return visited

    def main():
        '''
        1. Call Function Build graph.
        2. Then perform dfs on graph and check
            if goal or end is met.
        3. If 2. returns true then, is_Transformable
           else not.
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
