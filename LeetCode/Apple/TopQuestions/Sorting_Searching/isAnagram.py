#Given 2 strings s and t, write a function to deermine
#if t is an anagram of s.

#Example 1:
#INput s= "anagram", t = "nagaram"
#Output: true


#Example 2:
#INput S  = "rat", t = "car"
#Output: false


#Note:
#You may assume the string contains only lowercase
#alphabets.

#Follow up:
#What if the inputs contain unicode?
#I dont give a damn funck


#How do we tackle this?
#The question is whether the first string s
#is transformable to string t.

#Sorting approach, then compare. if true transformable, else not.
#Complexity of sorting O(n)logn
#Space Complexity: O(n)

#Hash table solution: Build hashtable : O(n)
#lookup into hash: O(1)

class Solution(object):
    def isAnagram(self,s:str,t:str)->bool:
        #Corner case:
        if len(s)==len(t):
            dictA = self.hashmap(s)
            print (dictA)
            dictB = self.hashmap(t)
            print (dictB)
            if dictA==dictB:
                return True
            else:
                return False
        else:
            return False


    def hashmap(self,words):
        dict = {}
        for i in words:
            if i not in dict:
                #counter = 1
                dict[i] = 1
            elif i in dict:
                dict[i]+=1
        return dict


#Approach 2:sort the 2 strings then compare them
class Solution_sort(object):
    def isAnagram(self,s:str,t:str)->bool:
        return False 


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    output = Solution()
    print ('Are the 2 strings anagram of each of other?',output.isAnagram(s,t))
