class PrettyMixin():
	def dump(self):
		import pprint
		pprint.pprint(vars(self))
class Thing(PrettyMixin):
	pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "elfritch"
t.dump()


class Car():
	def exclaim(self):
		print("I'm a car!")

a_car = Car()
a_car.exclaim()

class Duck:
	def __init__(self, input_name):
		self.name = input_name

fowl = Duck('Chicken')
print(fowl.name)
