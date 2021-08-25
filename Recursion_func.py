
# Error Test
#def dive():
#	return dive()
#
#print(dive())

# Flatting
def flatten(lol):
	for item in lol:
		if isinstance(item, list):
			for subitem in flatten(item):
				yield subitem
		else:
			yield item

lol = [1, 2, [3,4,5],[6,[7,8,9],[]]]
print(flatten(lol))
print(list(flatten(lol)))

