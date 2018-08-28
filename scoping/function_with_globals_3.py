# but what if you are like "I LOVE modifying global
# variables inside functions"?

a = 1

def my_function():
	global a
	a = 3
	print(a)

my_function()
print(a)