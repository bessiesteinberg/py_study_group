import time

def timeout(max_time): # decorator factory
	"""
	Returns string representing time to excecute some_function,
	unless max time is hit then an exception is raised
	"""
	def timing_function(some_function): # decorator
		"""
		Returns string representing time to excecute some_function()
		"""

		def wrapper(*args, **kwargs):
			before = time.time()
			some_function(*args, **kwargs)
			after = time.time()
			difference = after - before
			if difference > max_time:
				raise Exception("Timeout!")
			else:
				return "some_function() excuted in {}s".format(difference)

		return wrapper
	return timing_function

@timeout(.04)
def add_lots_of_numbers(nums):
	sumvals = 0
	for x in range(0, nums):
		sumvals += x

	print("sum of {} nums = {}".format(nums, sumvals))

# add_lots_of_numbers = timeout(0.04)(add_lots_of_numbers)

print(add_lots_of_numbers(10))
print("\n")
print(add_lots_of_numbers(10000000))


