'''
Ref: https://start.interviewing.io/interview/hz1Mo0I3a8j8/replay
'''


'''
For a given number target and error e,
find a square root x that satisfies
the following:
math.abs(x**2-target) < e


example squareRoot(target=100.0,error=2.0) --> 9.9**2 = 98.01

1. sqrt(100) = 10 
2. 9**2 = 81 

3. 2 boundaries: 9--10.
   9+10/2=9.5 --> small = 9.5, large = 10.0
   small = 9.5
   large = 10.0
   while error > 2.0
   --> Compute diff: 9.5**2 -10**2
       errpr = math.abs(10**2-small**2)
       small = large+small/2 

That should be it.
'''
import math
def squareRoot(target,error):
    high = math.sqrt(target)
    low = high-1
    eps = 20.0 #or any large number
    while eps > error:
        eps = abs(target-low**2)
        low = (low + high)/2
    return low

if __name__ == "__main__":
    target = 100
    error = 2.0
    closest_sqr = squareRoot(target,error)
    print ('closest square root',closest_sqr)



