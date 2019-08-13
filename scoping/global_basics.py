# global variables: are defined in the main body of a 
# file like the ones below

a = "I'm a string!"

for i in range(0, 5):
	# this is also a global variable
	b = 6

if True:
	c = 8

try:
	d = 9
except Exception:
	print("EXCEPTION!")

print("a: {}".format(a))
print("b: {}".format(b))
print("c: {}".format(c))
print("d: {}".format(d))
print("i: {}".format(i))



