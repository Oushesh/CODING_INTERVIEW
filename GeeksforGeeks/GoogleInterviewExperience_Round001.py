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
