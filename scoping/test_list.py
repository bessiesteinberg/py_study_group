def my_func(l=[]):

	l.append(9)
	print(l)
	return l

newl = my_func([])

for i in range(0,5):
	my_func()

print(newl)