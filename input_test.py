def commentary(color):
	if color == 'red':
		return "It's a tomato!"
	elif color == 'green':
		return "It's a green pepper!"
	elif color == 'bee_purple':
		return "What the fuxx is this?"
	else :
		return "That's weird,,,, I don't know that color " + color + "."

print(commentary('red'))
print(commentary('green'))
print(commentary('bee_purple'))
print(commentary('black'))

take_color = input('Input color please : ')
output = commentary(take_color)
print(output)
