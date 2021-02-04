#EntryLevelCodingSD1.py
#Reference to the interview: https://www.youtube.com/watch?v=595NTKwQbwY
'''
Fist we define the problem:
Amazon is building

'''
class StrringChecker():
	def __init__(self,rev,rep,query):
		self.rev = rev
		self.rep = rep
		self.query = query

	def 3KeySug(self):
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
	rev =
	rep =
	query =
	current_String = StrringChecker(rev,rep,query)
	print ('The output for the match is the following:',current_String.3KeySug)

