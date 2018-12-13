from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
	f = open(file_name, mode)
	try:
		yield f
		print("hello!")
	finally:
		print("hi")
		f.close()

try:
	with open_file('test.txt', 'w') as file:
		raise Exception("I AM A GREAT PROGRAMER")
except:
	print("exception was raised")
	# pass


# for x in range(10000):
# 	file_name = "foo{}.txt".format(x)
# 	with open_file(file_name, 'w') as file:
# 		# do stuff with the file
# 		pass

