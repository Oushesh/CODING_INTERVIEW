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
		#True: if all the keys have value 1.
		for key,value in map.items():
			while value==1:
				continue
			return True

	def PermutationsContainedInString(self):
		count = 0
		map = {i:0 for i in self.smallString} #initialise the map count to 0
		#initalised
		idx = 0
		while idx<len(self.smallString):
			map[self.bigString[idx]]+=1

		if self.map_check(map):
			count+=1 #update the count here

		#At this point: the map is already updated
		for i in range(1,len(self.bigString)-len(self.smallString)):
			#perform the check here
			if self.map_check(map):
				count+=1
				#decrease the count here by 1.
				map[self.bigString[i-1]]-=1 #remove the old counter
				map[self.bigString[i]]+=1   #add the new counter here.

		return count

if __name__ == "__main__":
	bigString = "cbabcacabca"
	smallString = "abc"

	current_problem = StringMatcher(bigString,smallString)
	print ('The number of permutations is',current_problem.PermutationsContainedInString())


#TODO: To check for edge cases for this code And to test it.
