#test_LandandSea.py



#parent = [i for i in graph.keys() if graph[i]==[b] or if [i in a for a in dict.values()]
'''
dict = {'a':[5,7],'b':[3],'e':[7]}

#query determine.
search_value = [5]

for key,value in dict.items():
    if search_value == value:
        #print (key) #parent
    if search_value[0] in value: #in case we have the number
        #print (key)
'''

def parent(graph,node):
    '''
    node as a single list element or List itself in case of multiple
    children
    '''
    for key,value in graph.items():
        if len(value)==1:
            if node == value:
                return key
        elif len(value)>1:
            if node[0] in value:
                print(key)
                return key



graph = {'a':['b','h'],'b':['c','d','e'],'e':['f','g'],'h':['i','j'],'k':['l'],'l':['m','n']}
node = ['l']

print(parent(graph,node))

#expected output is b
