drinks = {
	'martini' : {'vodka', 'vermouth'},
	'black russian' : {'vodka', 'kahlua'},
	'white russian' : {'cream', 'kahlua', 'vodka'},
	'manhattan' : {'rye', 'vermouth', 'bitters'},
	'screwdriver' : {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
	if 'vodka' in contents and not('cream' in contents or 'vermouth' in contents):
		print(name)


