

#define global parameter
animal = 'fruitbat'
def print_global():
	print('inside print_global: ', animal)

#print('at the top level: ', animal)

#print(print_global())

#If change global parameter
#def change_and_print_global():
#	print('inside_change_and_print_global: ', animal)
#	animal = 'wombat' #Change global paramer's value
#	print('after the change: ', animal)
#
#print(change_and_print_global())

def change_local():
	animal = 'wombat'
	print('inside change_local: ', animal, id(animal))

print(change_local())
print(animal)
print(id(animal))

# Evince global

def change_and_print_global():
	global animal # evince 'animal' parameter is global parameter
	animal = 'wombat'
	print('after the change: ', animal)

print(animal)

print(change_and_print_global())

print(animal)

# Using
animal = 'fruitbat' #global
def change_local():
	animal = 'wombat' # local
	print('locals:', locals())

print(animal, sep='\n')

print(change_local(), sep='\n')

print('globals:', globals(), sep='\n')

print(animal)

