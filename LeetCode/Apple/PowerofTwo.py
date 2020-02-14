class Solution:
    def isPowerofTwo(self,n:int) -> bool:
        if n==1:
            return True #Case for 2^0 =1
        else:
            while (n%2==0):
                n=n/2
                return True
            return False

if __name__ == '__main__':
    #n = 16
    n = 1
    n  = 5
    object = Solution()
    print (object.isPowerofTwo(n))
