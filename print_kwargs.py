# Keyword argument
def print_kwargs(**kwargs):
	print('Keyword arguments: ', kwargs)

print('print_kwargs()')
print_kwargs()

print('print_kwaargs(~~~~~~~~)')
print_kwargs(wine='merlot', entree='mutton', dessert='marcaroon')

# Keyword_only arguments
def print_data(data, *, start=0, end=100):
	for value in (data[start:end]):
		print(value)

data = ['a','b','c','d','e','f']

print('print_data(data)')
print_data(data)

print('print_data(data, start=4)')
print_data(data, start=4)

print('print_data(data, end=2)')
print_data(data, end=2)

