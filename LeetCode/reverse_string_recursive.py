'''
Write me a program
that reverse string within brackets

'cat(dog)cow' --> catgodcow

'ca(t(dog)c)ow' --> cacdogtow


'''

class Solution():
    def reverse_string(self,string):
        split = string.split('|')

        for i in range(1,len(split)-1):

        ''.join([i for i in split])
        return output

    def main(self,string):

        return None

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
    print (output.reverse_string(s1))
    print (output.reverse_string(s2))
