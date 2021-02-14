'''
#https://www.youtube.com/watch?v=tOD6g7rF7NA
'''

class String():
    def __init__(self,s,t):
        self.s = s
        self.t = t

    def subarray_check(self,s,t,left,right,count):
        if s[0:left+1] in t and s[left:right] in t:
            count+=1
            return True,count
        else:
            return False,count

    def check(self):
        left = 0 #beginning index
        right = len(self.s) #at the end of the string
        count = 0
        #Inspired by binary search algorithm
        while (left<right):
            if self.subarray_check(self.s,self.t,left,right,count)[0]:
                return self.subarray_check(self.s,self.t,left,right,count)[1]
            else:
                #need to check
                left+=1
                count=self.subarray_check(s,t,left,right,count)[1]

                right-=1
                count=self.subarray_check(s,t,left,right,count)[1]
            return count

if __name__ == "__main__":
    s = '3145926535897946262433832789'
    t = ['3','314','31','59','49','9001','159265897']
    current_string = String(s,t)
    print ('The minimum count needed to spilt the string is:',current_string.check())
