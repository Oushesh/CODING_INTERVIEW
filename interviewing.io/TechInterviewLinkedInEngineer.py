'''
Online Coding Interview:
link:https://www.youtube.com/watch?v=aotBpjJUqJo
'''
#Array
#Basically moving the letters around.
'''
Input:
['perfect makes practice']
Output:
['practice makes perfect']
'''

'''
What about time and space complexity?
Time and Space complexity for this idea.
How about reversing the whole string first?
The aim is to reverse without anything extra.
-->This we can do.
-->Then reverse each words in the reversed string.
'''

class Solution:
    def reverse_Word(self,input):
        inputWords = input.split(" ") #find invdividual words
        inputWords = inputWords[::-1]
        # now join words with space
        output = ' '.join(inputWords)
        return output

class Solution_list:
    #reverse each words in the list.
    #reverse the total list
    def reverse_word(self,input):
        #Get inputWordss
        start = 0
        end   = 1
        for i in range(len(input)):
            while input[i]!=' ':
                end+=1
            input[:]=input[start:end] #reverse just part of the string
            
        return output


if __name__ == "__main__":
    input_list = ['p','e','r','f','e','c','t',' ','m','a','k','e','s',' ','p','r','a','c','t','i','c','e']
    input = 'perfect makes practice'
    object = Solution()
    print ('The reversed words are:', object.reverse_Word(input))

    object_list = Solution_list()
    print ('The reversed words for the input list data type:',object_list.)
