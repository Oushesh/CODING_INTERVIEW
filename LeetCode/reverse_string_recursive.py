'''
Write me a program
that reverse string within brackets
'cat|dog|cow' --> catgodcow
'ca|t|dog|c|ow' --> cacdogtow
'''

class Solution():
    def spliter(self,string):
        return string.split('|')

    def reverse_substring(self,substring):
        return substring[::-1]

    def join(self,splits,reversed,left,right):
        return splits[left]+reversed+splits[right]

    def reverse(self,splits):
        # we will always have odd number of splits
        # since we have to have an even number of openings+closures
        mid_index   = int(len(splits)/2) # 0-index based
        start_index = 0
        end_index   = len(splits)-1
        #we then take the middle, reverse it.
        #combine it with 2 items next to it and then re-reverse
        #continue until we reach the start index and end_index

        left   = mid_index
        right  = mid_index
        target = splits[mid_index]
        while (not left==start_index or not right==end_index):
            reversed = self.reverse_substring(target)
            left  -=1
            right +=1
            target = self.join(splits,reversed,left,right)
        return target

    def main(self,string):
        splits = self.spliter(string)
        output = self.reverse(splits)
        return output


if __name__ == "__main__":
    s1 = 'cat|dog|cow'
    '''
    ['cat', 'dog', 'cow']
    '''
    '''
    ['ca', 't', 'dog', 'c', 'ow']
    '''
    s2 = 'ca|t|dog|c|ow'
    #separator = '()'
    output = Solution()
    print (output.spliter(s2))

    splits = ['ca', 't', 'dog', 'c', 'ow']
    print (output.main(s2))
