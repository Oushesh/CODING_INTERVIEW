###Reference: https://www.geeksforgeeks.org/google-interview-experience-on-site-for-sde/

'''
Google Interview Experience | On-Site for SDE
Difficulty Level: Hard
'''


'''
Round 1: There are several equations given in terms of 2 variables
with a '<' or '>' sign between them. Ex-a>b, b>c etc...
You have to answer whether there is a sequence which of the
variables which will satisfy all the equations given.
'''

'''
How to do this?
List: a,b,c,d,e,f,g

a>b, b>c, c>d, e<c, f>g,

1. The ones which do not have condition we leave it.
2. Focus on those which do not have condition.


Simpler problem:
Global order, i<i+1<i+2<i+3<.....n
min = '-inf'


10,5,6,7,8,9,1,3
i= 0
1. 10>5, 10<5 -->swap(a,b) 5,10, i=1
2. 1>3, 1<3 --> sawp(a,b) 1,3, j=len(n),-->j--, j=j-1, max = 3
3. 9>3, swap(9,3)-> 1,3,9, max = 9
4. O(n)


Likewise, we use but instead here we query the condition from a list.
And we solve in O(n)
'''


#TODO: Being done now


class Inequality:
    def standardise(self,conditions):
        '''
        We define standardisation as the
        setting all the inqeuality to <
        '''
        for condition in conditions:
            if condition[1]=='>':
                condition[1]='<'
                condition[0],condition[2]=condition[2],condition[0] #swap them
        return conditions

    def contradiction(self,conditions):
            #return True
        return False

    def con_len(self,var,conditions):
        '''
        7--> 21, 6+5+4+3+2+1 = 21
        '''
        num = len(var)
        sum = 0
        while (not num<=1):
            sum+=num
            num -=1
        return sum==len(conditions)

    def var_freq(self,conditions):
        '''
        The frequency counter is just a dictionary.
        '''
        freq = {}
        for var in conditions:
            if var[0] not in freq:
                freq[var[0]]=1
            else:
                freq[var[0]]+=1 #update the count
            if var[2] not in freq:
                freq[var[2]]=1
            else:
                freq[var[2]]+=1 #update the count

        #Sort the frequency counter

        return freq

    def main_check(self,var,conditions):
        #1-Standardise the conditions.
        #2-Check length of conditions after standardisation, if less ()
        #3-Check condradiction.
        #4-perform alignment
        standardised_conditions = self.standardise(conditions)
        if not self.con_len(var,standardise_conditions) and not self.contradiction(standardised_conditions):
            '''
            Perform checking whether we find a unique order of element
            Find the variable with least conditions from the sorted freq counter.
            '''






if __name__ == "__main__":
    '''
    Given a list of integers and inequalities, output the overall inequality
    equation if possible else return False
    '''
    var = ['a','b','c','d','e','f','g']
    conditions = [('a','<','g'),
    ('a','<','f'),
    ('a','<','e'),
    ('a','<','d'),
    ('a','<','c'),
    ('a','<','b'),
    ('b','<','g'),
    ('b','<','f'),
    ('b','<','e'),
    ('b','<','d'),
    ('b','<','c'),
    ('c','<','g'),
    ('c','<','f'),
    ('c','<','e'),
    ('c','<','d'),
    ('d','<','e'),
    ('d','<','f'),
    ('d','<','g'),
    ('e','<','f'),
    ('e','<','g'),
    ('f','<','g')]

    ineq = Inequality()
    print ('The standardised conditions is:',ineq.)

    print ('The number of conditions given are insufficient to derive the overall inequality:',ineq.check_con_)


#####TODO: 1. Return sorted_freq_counter, update the connter and sort the rest
