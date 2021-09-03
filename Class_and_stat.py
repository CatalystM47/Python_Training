class Fruit:
	color = 'red'

blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)

Fruit.color = 'orange'
print(Fruit.color)

print(blueberry.color)
new_fruit = Fruit()
print(new_fruit.color)
