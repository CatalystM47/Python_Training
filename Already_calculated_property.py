
class Circle():
	def __init__(self, radius):
		self.radius = radius
	@property
	def diameter(self):
		return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.diameter)

# Name mangling
class Duck():
	def __init__(self, input_name):
		self.__name = input_name
	@property
	def name(self):
		print('inside the getter')
		return self.__name
	@name.setter
	def name(self, input_name):
		print('inside the setter')

		self.__name = input_name

fowl = Duck('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name

print("########")
#fowl.__name
print(fowl._Duck__name)
