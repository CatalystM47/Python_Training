
#Generator range
print(sum(range(1, 101)))

# build rnage func
def my_range(first=0, last=10, step=1):
	number = first
	while number <= last:
		yield number
		number = number + step

print(my_range())

ranger = my_range(1, 5)
print(ranger)

for x in ranger:
	print(x)

# Gen comprihension

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))

print(genobj)

for thing in genobj:
	print(thing)

# Decorator
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function: ', func.__name__)
		print('Positional arguments: ', args)
		print('Keyword arguments: ', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function
# If you transfer any func name at dcoument_it() func as argument, anyway you can get new func what have additional statement
# It didn't run on func function but, call from document_it() func and get new return value and new function

# Use Decorator
def add_ints(a,b):
	return a + b

print(add_ints(3,5))

cooler_add_ints = document_it(add_ints) # Decorator Manual assignment
print(cooler_add_ints(3,5))


def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		return result * result
	return new_function

# duplicate apply Decorator
@document_it
@square_it
def add_ints(a,b):
	return a + b

print(add_ints(3,5))


