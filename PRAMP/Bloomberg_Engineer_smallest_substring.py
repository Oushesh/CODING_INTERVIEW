#Reference: https://www.youtube.com/watch?v=5xuvqBjRkok


'''
input: arr = ['x','y','z'], str = 'xyyzyzyx'
output: 'zyx'
'''

'''
my Thought Patterns:
Lets do it with 2 pointers. Where to start and
where to end:
Loop over the string:
start = 0
end   = 1 --> keep on looping if the character is in arr,
First solution we have: xyyz (This is not the smallest), put a
Keep count of how many times we encountered x,y,z Hash Table.
'''
class Solution():
    '''
    hash_check checks that hash count is >1
    '''
    def hash_check(self,dict):
        dict = {}
        for key,value in dict.items():
            if not value > 0:
                return False
        return True

    def max_subarray(self,str,array):
        start_index = 0
        end_index   = 0
        #build hashmap with keys from arr and corresponding value = 0
        #shortest string implies hash[x:1,y:1,z:1]
        dict        = {i:0 for i in arr}
        solution = []
        for i in range(len(str)):
            if str[i] in array:
                dict[str[i]] +=1
                if not self.hash_check(dict):
                    end_index +=1
                    while (start_index<end_index):
                        '''
                        increase start_index by 1
                        decrease the count of the dict.
                        '''
                        dict[str[start_index]]-=1
                        if not self.hash_check(dict):
                            start_index +=1

            else:
                start_index+=1
                end_index+=1
        return array[start_index:end_index]


if __name__ == "__main__":
    str  = 'xyyzyzyx'
    arr  = ['x','y','z']
    output = Solution()
    print (output.max_subarray(str,arr))
