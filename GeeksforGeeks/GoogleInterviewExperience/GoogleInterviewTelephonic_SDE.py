'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-telephonic-sde/?ref=rp

Round 1:
The interviewer was friendly.

Question:  Basically, the question was that you are given a phone
screen with height H and certain width W. You have to fit some
text into the screen. Give the maximum size of letters that
one can have such that text fits into the screen.


1. Lets assume we have list: size = [s1,s2,...,sn]

   Approach 1: Brute Force. We actually fit all the sizes from smallest to largest
  and see which one works.
   We would need to sort the list beforehand: O(logn), Then reloop over the sorted
   list O(n) and see which one fits until we reach the largest.

   In this case: Worst Case Time Complexity:  O(nlogn)+ O(n) All fit until the end from smallest
   to largest such that we would need to traval the entire list to get find the answer


2. Interviewer asks: Can you make it better? Yeah lets see. Lets try to sort and loop at the same time.
   Instead of sorting then re-looping throughout the entire lets use Binary Search.

   Binary Search: We choose the middle and see if it fits (fill the screen with it.)
   --> If it does we choose the lower half, else choose the upper half.
       Iterate until break. O(n) time complexity, Space complexity is O(1) since
       we will need only variables, no extra array storage.
'''
