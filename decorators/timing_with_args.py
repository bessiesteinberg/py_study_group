import time

def timing_function(some_function):
	"""
	Returns string representing time to excecute some_function()
	"""

	# def wrapper():
	def wrapper(*args, **kwargs):
		before = time.time()
		# some_function()
		some_function(*args, **kwargs)
		after = time.time()
		difference = after - before
		return "some_function() excuted in {}s".format(difference)

	return wrapper

@timing_function
def add_lots_of_numbers(nums):
	sumvals = 0
	for x in range(0, nums):
		sumvals += x

	print("sum of {} nums = {}".format(nums, sumvals))

print(add_lots_of_numbers(10))
print("\n")
print(add_lots_of_numbers(1000000))



