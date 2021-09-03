
#class Word():
#	def __init__(self, text):
#		self.text = text
#	def equals(self, word2):
#		return self.text.lower() == word2.text.lower()

class Word():
	def __init__(self,text):
		self.text = text
	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('Ha')
third = Word('eh')

#print(first.equals(second))

#print(first.equals(third))

print("########")

print(first == second)
print(first == third)

first
print(first)
