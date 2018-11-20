# at least a context manager is a class that has
# __enter__() and __exit__() defined

# for example, let's pretend that this is helpful

class File():

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		print("{} calling __enter__...".format(str(self)))
		self.open_file = open(self.filename, self.mode)
		return self.open_file

	def __exit__(self, *args):
		print("{} calling __exit__...".format(str(self)))
		self.open_file.close()

	def __str__(self):
		return "File [{}]".format(self.filename)


for x in range(10000):
	file_name = "foo{}.txt".format(x)
	with File(file_name, 'w') as f:
		f.write(file_name)