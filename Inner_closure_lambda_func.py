
# Inner function
def outer(a, b):
	def inner(c, d):
		return c + d
	return inner(a, b)

print(outer(4,7))

# String Inner function
def knights(saying):
	def inner2(quote):
		return "We are the knights who say: '%s'" % quote
	return inner2(saying)

print(knights('U-ra!'))

# Closure func
def knights2(saying):
	def inner3():
		return "We are the knights who say: '%s' " % saying
	return inner3

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a)
print(b)

print(a())
print(b())

# Lambda func
def edit_story(words, func):
	for word in words:
		print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word): #first letter make bigger and attach !
	return word.capitalize() + '!'

print(edit_story(stairs, enliven))

print(edit_story(stairs, lambda word: word.capitalize() + '!'))
