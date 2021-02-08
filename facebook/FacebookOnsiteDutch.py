'''
FacebookOnsiteDutch Nationl Flag Variation Problem

Ref: https://leetcode.com/discuss/interview-question/algorithms/124623/facebook-onsite-variation-of-dutch-national-flag-problem

You have an unsorted array of integers and a function
string getCategory(integer), which deterministically returns 1 of three possible strings: "low", "medium", or "high", depending on the input integer. You need to output an array with all the "low" numbers at the bottom, all the "medium" numbers in the middle, and all the "high" numbers at the top. This is basically a partial sort. Within each category, the order of the numbers does not matter.

For example, you might be give the array [5,7,2,9,1,14,12,10,5,3].
For input integers 1 - 3, getCategory(integer) returns "low", for 4 - 10 it returns "medium," and for 11 - 15 it returns "high".

You could output an array (or modify the given array) that looks like this: [3,1,2,5,5,9,7,10,14,12]
'''

class Integers():
	def sort(self,numbers):
		return sorted

if __name__ == "__main__":
	numbers =  [5,7,2,9,1,14,12,10,5,3]
	given_Int = Integers()
	print ('The sorted numbers are:',given_Int.sort(numbers))