'''
Reference: https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/?ref=lbp
Reference: http://www.learn4master.com/algorithms/aho-corasick-algorithm
Algorithm Time Complexity: O(len(text)+len(pattern)+len(output_matches))
Naive Search would result in O(len(text)²) computational Complexity
This algorithm is good for searching for continuous set of patterns.
Applications of this algorithm: Finding every sequence of substring
from the given main string

1. Build the Tri from dictionary
2. GoTo Function: traverse save Failures set of outputs
3. GoTO Function
'''

class Node():
    def __init__(self,label):
        self.label = label
        self.map = {} #Dictionary containing the graph map
        self.fail = None
        self.output = set()

    def get_label(self):
        return self.label

    def get_children(self):
        #get keys,values
        return self.map.items()

    def get_child(self,word):
        return self.map[word]

    def add_output(self,word):
        return self.output.add(word)

    def get_output(self):
        return self.output

    def add_child(self,word):
        if self.map.get(word):
            return self.map[word]
        else:
            #create a new node
            new_node = Node(word)
            self.map[word] = new_node
        return new_node

    def get_fail(self):
        return self.fail

    def set_fail(self,f):
        self.fail = f
        return None

    def is_world(self):
        return bool(self.output)

    def get_child(self,word):
        return self.map.get(word) #dict.get(word) vs dict[word]-> .get is able error should the dict not contain the key

    def get_or_add_child(self,word):
        parent = self.get_child(word)
        if not parent:
            parent = self.add_child(word)
        return parent

class AhoCorasick():
    #Traversal Function, need to save all the failures and the output as well.
    #we need Funtion, needing this:
    def __init__(self):
        self.root = Node('-1')
        self.has_built = False

    def add_word(self,word):
        parent = self.root
        for i in range(len(word)):
            current = word[i]
            parent = parent.get_or_add_child(current)
            if i == len(word)-1:
                parent.add_output(word)

    def buildAutomaton(self):
        self.root.set_fail(self.root)
        queue = []
        children = self.root.get_children()
        for key,value in children:
            value.set_fail(self.root)
            queue.append(value)

        while queue:
            parent = queue.pop()
            for key,value in parent.get_children():
                queue.append(value)
                pf = parent.get_fail()
                pfc = pf.get_child(key)
                while not pfc and not pf==self.root:
                    pf = pf.get_fail()
                    pfc = pf.get_child(key)
                if pfc:
                    value.set_fail(pfc)
                else:
                    value.set_fail(self.root)

    def build(self,words):
        for word in words:
            self.add_word(word)
        self.buildAutomaton()
        self.has_built = True
        return None

    def traverse(self,word):
        parent = algorithm.root #starting point
        i = 0
        result  = []
        while i < len(word):
            current = word[i]
            #children is the value of the key
            pc = parent.get_child(current)

            while not pc:
                parent = parent.fail()
                pc = parent.get_child(current)
                if parent == self.root and not pc:
                    i+=1
                    break
                if pc:
                    parent = pc
                    i+=1
                    result.extend(parent.get_output())
        return result

if __name__ == "__main__":
    chars = cur.get_children_chars()
    for c in chars:
        c_state = cur.get_state(c)
        f = cur.get_fail()
        fc = f.get_state(c)
        while fc is None and f != root:
            f = f.get_fail()
            fc = f.get_state(c)
    if fc:
        c_state.fail = fc
    else:
        c_state.fail = root

    dictionary = ['he','she','his','her','hers']
    algorithm = AhoCorasick()
    algorithm.build(dictionary)
    result = algorithm.traverse('shherishers')

    print ('The result is:',result)
    result2 = algorithm.traverse('shershehishers')
    print ('The result is:',result2)


#Reference: http://www.learn4master.com/algorithms/aho-corasick-algorithm
