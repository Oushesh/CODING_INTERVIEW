#Reference: 'interviewing.io'
#Changing one word from a dictionary to a different one

#Extended to the TUM assignement for Jadaav
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
    #This one is more efficient
    def difference_set_method(self,word1,word2):
        '''
        Use set method and perform intersection
        with set operation coz its easier
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
        '''
        Looping creates possibilities of all possible pairs here
        '''
        for i  in range(len(dictionary)):
            for j in range(len(dictionary)):
                #Call the function differby1 letter here: if True then add it as neighbour
                #Avoid duplicates of the the candidates
                if self.difference(dictionary[i],dictionary[j]) and not dictionary[i]==dictionary[j]:
                    #graph[dictionary[i]].append(dictionary[j])
                    graph[dictionary[i]].add(dictionary[j])
        return graph

    def DFS(self,graph,start,visited=None):
        if visited is not None:
            visited = set()
        visited.add(start)
        #Traverse the graph
        for neighbours in graph[start] - visited:
            self.DFS(graph,start,visited)
        return visited

    def DFS_path_recursive(self,graph,start,goal,visited=None):
        '''
        Take the DFS approach. Traverse the graph,
        while goal not met:
            stack all nodes visited, path needed:
        '''
        if visited is not None:
            visited = set()
        visited.add(start)


        return None

    def DFS_path(self,graph,start,goal):
        '''
        return of all possible paths
        Here we use a list of lists to represent the outptut
        with the first as current node and
        the other one is
        '''
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                #check if goal is reached
                if next == goal:
                    yield  path + [next] #build the path
                else:
                    stack.append((next, path + [next]))
        return None

    '''
    path exists determine if the words are transformable
    from start to endnode
    '''
    def path_exist(self,generated_paths):
        '''
        Boolean saying whether path exists or not.
        '''
        if len(generated_paths):
            return True
        return False

if __name__ == "__main__":
    dictionary = ['dog','cat','hot','hog','eat','dug','dig','hat']
    '''
    example: start: 'dog', end: 'hat'
    #Path then is: 'dog'-> 'dot'-> 'hot'->'hat'
    Function should return true if a path is found
    else  false
    '''
    start = 'dog'
    end   = 'hat'
    current_game = Word()
    current_graph = current_game.build_graph(dictionary)
    print ('The adjacency graph from the dictionary words are as follows:',current_graph)

    generated_paths = list(current_game.DFS_path(current_graph,start,end))

    print ('The path from start node to end node is as follows:',generated_paths)
    print ('Does a path from the given start node to the goal node?:', current_game.path_exist(generated_paths))
