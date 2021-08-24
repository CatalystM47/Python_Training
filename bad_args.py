# Change args (strictly....It should not)
outside = ['one','fine','day']
def mangle(arg):
	arg[1] = 'terrible!'


#print('outside')
print(outside)

#print('mangle(outside)')
mangle(outside)
print(outside)
