END_MARK = '*'
class Trie:
    def __init__(self, val):
        self.val = val
        self.adjacentChars = {}

class StreamChecker:
    def __init__(self, words):
        self.cache = set() # Space O(num of words * avg word length)
        self.hashTable = {} # Space O(num of words * avg word length)
        # Build Trie
        for word in words: # Time O(num of words * avg word length)
            firstChar = word[0]
            if not firstChar in self.hashTable:
                self.hashTable[firstChar] = Trie(firstChar)
            node = self.hashTable[firstChar]
            for c in word[1:]:
                if not c in node.adjacentChars:
                    node.adjacentChars[c] = Trie(c)
                node = node.adjacentChars[c]
            node.adjacentChars[END_MARK] = None

    def query(self, letter):
        found = False
        newCache = set()
        for node in self.cache: # Time O(num of words)
            if letter in node.adjacentChars:
                newCache.add(node.adjacentChars[letter])
                if END_MARK in node.adjacentChars[letter].adjacentChars:
                    found = True
            # else: don't need to keep any more because it will not be continous

        if letter in self.hashTable:
            # From start
            newCache.add(self.hashTable[letter])
            if END_MARK in self.hashTable[letter].adjacentChars:
                found = True
        self.cache = newCache
        return found

if __name__ == "__main__":
    END_MARK = '*'
    words=["cd","f","kl"]
    current_stream = StreamChecker(words)
    print (current_stream.query('a'))

    print (current_stream.query('d'))
