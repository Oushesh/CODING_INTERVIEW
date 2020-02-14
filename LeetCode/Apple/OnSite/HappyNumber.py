#Example
#Input: 19
#Output: true
#Explanation:
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash = {}
        while True:
            if n not in hash:
                hash[n]= n
                n = sum([int(x)**2 for x in list(str(n))])
                if n == 1:
                    return True
            else:
                return False

if __name__ == '__main__':
    n = 19
    n = 20
    object = Solution()
    print (object.isHappy(n))
