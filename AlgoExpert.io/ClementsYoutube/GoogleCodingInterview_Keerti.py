'''
GoogleCodingInterview_Keerti

bigString = "cbabcacabca"
smallString = "abc"

output: 6 #"cba", "abc", "bca", "cab", "abc", "bca"

#initialisation take care
Loop(len(smallString),len(bigString))
count = 0
Sliding WIndow: cba
#c: 1
#b: 1
#a: 1

#count+=1 --> decrease the count of c by 1.
#c: 1-1 = 0
#b: 2
#a: 1

pop_the last element.
Iteration 3: (abc) -->
#c: 1
#b: 2-1 = 1
#a: 1
#check(dict)

overlapping. There is string overlpaing.

1. Approach 1: From small string--> all possible combinations.
   Search for all combinations in the string.
   len(smallString),m --> m! search n times along length(m string)
   O(mxn) --> Further simplified only and if only: m<<n
   O(n)  --> O(n²) worst case

2. Do it in 1 loop only. Build a dict_count
   dict = {'a':0,'b':0, 'c':0}
   #initialised.

   if dict[element]==0:
   	we continue.

'''


class StringMatcher():
	def __init__(self,bigString,smallString):
		self.bigString = bigString
		self.smallString = smallString

	def map_check(self,map):
		#input has to be a valid map
		#loop until
		for key in map.keys:
			 not map[key]==1:

		return True

	def PermutationsContainedInString(self):
		map = {i:0 for i in self.smallString} #initialise the map count to 0
		for i in range(len(self.smallString),len(self.bigString)):
			#perform the check here




if __name__ == "__main__":
	bigString = "cbabcacabca"
	smallString = "abc"

	current_problem = StringMatcher(bigString,smallString)
	print ('The number of permutations is',current_problem.PermutationsContainedInString())