'''
Reference: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
'''

#Our aim here is to take the

def trie(word):
    root = dict()
    for word in word_list:
        current = root




if __name__ == "__main__":
    words = ['bear','bell','bid','bull','buy','sell','stock','stop']
    #Trie is something like this:

    word_list = ["gold", "goal", "sole']
    #output: {'g': {'o': {'l': {'d': {}}, 'a': {'l': {}}}}, 's': {'o': {'l': {'e': {}}}}}
    #or another way could be:
    #{'g':['o'],'o'}
