import time

def timing_function(some_function):
	"""
	Returns string representing time to excecute some_function()
	"""

	def wrapper():
		before = time.time()
		some_function()
		after = time.time()
		difference = after - before
		return "some_function() excuted in {}s".format(difference)

	return wrapper

@timing_function
def add_lots_of_numbers():
	sumvals = 0
	for x in range(0, 1000000):
		sumvals += x

	print("sum = {}".format(sumvals))

print(add_lots_of_numbers())