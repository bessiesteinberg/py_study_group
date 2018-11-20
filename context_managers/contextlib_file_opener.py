from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
	f = open(file_name, mode)
	yield f
	f.close()

for x in range(10000):
	file_name = "foo{}.txt".format(x)
	with open_file(file_name, 'w') as file:
		# do stuff with the file
		pass

