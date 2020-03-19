#Reference: https://www.youtube.com/watch?v=wyu6VRmtCmE&t=170s

'''
function takes in 2strings and says whether they are equal
'''


class Solution():
    def compare(self,s1,s2):
        if s1.lower() == s2.lower():
            return True
        return False


if __name__ == "__main__":
    s1 = 'abc'
    s2 = 'ABc'
    output = Solution()
    print (output.compare(s1,s2))
    
