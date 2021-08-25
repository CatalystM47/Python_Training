
# class inherit
class Car():
	def exclaim(Self):
		print("I'm a Car!")

#class Yugo(Car):
#	pass
#print(issubclass(Yugo,Car))

#give_me_a_car = Car()
#give_me_a_yugo = Yugo()
#give_me_a_car.exclaim()
#give_me_a_yugo.exclaim()

# Method override

class Yugo(Car):
	def exclaim(self):
		print("I'm a Yugo! Much like a car, but more Yugo-ish.")
	def need_a_push(self):
		print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Person():
	def __init__(self, name):
		self.name = name

class MDPerson(Person):
	def __init__(self, name):
		self.name = "Doctor" + name

class JDPerson(Person):
	def __init__(self, name):
		self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)

print(give_me_a_yugo.need_a_push())
