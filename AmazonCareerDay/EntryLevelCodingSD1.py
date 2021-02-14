#EntryLevelCodingSD1.py
#Reference to the interview: https://www.youtube.com/watch?v=595NTKwQbwY
'''
Fist we define the problem:
Amazon is building some stuffs
'''
class StrringChecker():
	def __init__(self,rev,rep,query):
		self.rev = rev
		self.rep = rep
		self.query = query

	def ThreeKeySug(self):
		outputs = []
		lower_rep = sorted([word.lower() for word in self.rep])

		for i in range(1,len(self.query)):
			subQuery = self.query[0:i+1].lower()
			matchedWords = []
			for word in lower_rep:
				if word.startswith(subQuery):
					matchedWords.append(word)
				if len(matchedWords)==3:
					break
				if len(matchedWords) > 0:
					outputs.append(matchedWords)
		return outputs
if __name__ == "__main__":
	#rev: numreviews: 5
	#rep: repository: ["mobile","mouse","moneypot","monitor","mousepad"]
	#query: customerQuery: "mouse"

	#Example 2:
	#rev: 5
	#["code","codePhone","coddle","coddles","codes"]
	#query: coddle
	rev = 5
	rep = ["code","codePhone","coddles","codes"]
	query = "coddle"
	current_string = StrringChecker(rev,rep,query)

	#print (current_string.rev,current_string.rep,current_string.query)
	print (len(current_string.ThreeKeySug()))
	print ('The output for the match is the following:',current_string.ThreeKeySug())
