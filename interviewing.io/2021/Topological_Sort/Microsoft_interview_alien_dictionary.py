from collections import defaultdict
'''
default dict of set is same as:
'''
def freq(words):
    alphabets = {}
    for word in words:
        for c in word:
            if c not in alphabets:
                alphabets[c] = 1
            alphabets[c] += 1
    return alphabets

# 4. dfs algorithm with graph coloring to detect cycles
def dfs(node,visited,ans):
    if node in visited:
        return visited[node]
    visited[node] = False  # processing
    for nei in graph[node]:
        if not dfs(nei,visited,ans):
            return False  # loop found
    visited[node] = True  # processed
    ans.append(node)  # 5. Add a char to ans whenever there are no more outgoing edges
    return True

def topological(words, graph):
    alphabets = set([c for word in words for c in word])
    print(alphabets)
    for word1, word2 in zip(words, words[1:]):
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                graph[c2].add(c1)

                break
        else:
            if len(word1) > len(word2):
                return ''  # edge case 'app', 'apple'
    print ('The current graph is:', graph)
    ans = []
    visited = {}

    # 6. do dfs for all chars in alphabet
    for c in alphabets:
        if c not in visited:
            if not dfs(c,visited,ans):
                return ''
    return ''.join(ans)

words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
graph = defaultdict(set)
print ('The graph built:',graph)
print(topological(words,graph))
print(freq(words))


#interviewing.io