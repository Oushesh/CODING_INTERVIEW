#O(N)Log(N)
#What tot know in Python?
#defualt list,list.sort(key= lambda;),Counter, enumerate,
import collections
class Solution:
    def topKFrequent(self, nums, k: int):
        my_dictionary = collections.Counter(nums) # Makes a dictionary from the input array
        print (my_dictionary)
        new_list = sorted(my_dictionary,key = lambda inp: my_dictionary[inp] ,reverse = True) # Outputs a list by sorting the dictionary based on its values which are the number of occurance
        return new_list[:k] # Return the k first elements of the list

class Solution_Hash_Table(object):
    #build a hash table
    def hash_table(self,words):
        dict = {}
        for i in words:
            if i not in dict:
                counter = 1
                dict[i] = counter
            elif i in dict:
                dict[i]+=1
        return dict

    def sorted_hash(self,hash):
        for i in len(hash)-1:
            if hash[i].values()==hash[i+1].values():
                if hash[i].keys()<hash[i+1].keys():
                    #swap the values
        return sorted_hash

    def topKFrequent(self,words,k):
        hash = self.hash_table(words)
        #sort hash
        sorted_hash = sorted(hash,key = lambda i:hash[i],reverse=True)
        print ('sorted_hash',sorted_hash)
        return sorted_hash[:k]

class Solution_Heap()

if __name__ == '__main__':
    k = 2
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    object = Solution()
    print (object.topKFrequent(words,k))

    #my Solution
    output = Solution_Hash_Table()
    print (output.topKFrequent(words,k))
