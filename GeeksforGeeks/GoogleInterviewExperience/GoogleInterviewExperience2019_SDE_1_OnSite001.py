'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/?ref=rp

Google Interview Experience for SDE-1

Problem Definition:

 X  is a good number if after rotating each digit individually by 180 degrees,
 we get a valid number that is different from X.  Each digit must be rotated –
 we cannot choose to leave it alone. 0, 1, and 8 rotate to themselves;
 6 and 9 rotate to each other, and the rest of the digits  do not rotate to
 any other valid digit. Range is given and you need to find out good numbers
 lie within that range.

Cases:
10 will be converted into 01 but not valid as our range start with 1. Prefix 0’s are not allowed.
If range is 1 to 7 and no 6 become 9 so it won’t allowed.
11 won’t allow as 11 will become same after change.
If no has digits like 2, 3, 4, 5, 7 then that no won’t allow.
Input: range: 1 to 10 (1 and 10 both are included)
Output: list of valid numbers: 6, 9
'''

class MarathonNumbers():
    def __init__(self,number,interval):
        self.number = number
        self.interval = interval
        self.min = interval[0]
        self.max = interval[1]

    #Output is a dict with key as input number & value  as rotated number
    def rot_complement(self):
        rot = {}
        primary = [i for i in range(10)]
        #Hard code the rules here:
        for num in primary:
            if num==0 or num==1 or num==8:
                rot[num]=num
            elif num==6:
                rot[num]=9
            elif num==9:
                rot[num]=6
            else:
                rot[num]='undef'
        return rot

    def rotate(self,num,rot):
        #Query to get the rotated complement from rot_complement dict
        if num in rot.keys():
            return rot[num]
        else:
            return None

    #is_good is a function that returns boolean True or False
    def is_good(self):
        #Build the rotated complement dict
        rot = self.rot_complement()

        #get the rotated_Numbers if in boundary and convert to int from string in 1 go
        '''
        Split the numbers then pass int(individually) into dict and get the output.
        '''
        for i in self.number:
            if int(i)>=self.min and int(i)<=self.max:
                if int(i) in rot:
                    if rot[int(i)]=='undef':
                        return False
        return True

    def mirrored_number(self):
        output = []
        rot = self.rot_complement()
        for i in self.number:
            print (i)
            if int(i)>=self.min and int(i)<=self.max:
                if int(i) in rot:
                    if not rot[int(i)]=='undef':
                        output.append(rot[int(i)])

        return output


if __name__ =="__main__":
    number  = '89' #as a string first
    #number = '77'
    min = 0
    max = 10
    interval = [min,max]
    marathon_run = MarathonNumbers(number, interval)
    print ('The number is a marathon number',marathon_run.is_good())
    print ('The mirrored_number is:',marathon_run.mirrored_number())

#TODO: C++ add the work here
