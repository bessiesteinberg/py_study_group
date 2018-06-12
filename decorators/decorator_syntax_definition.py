def simple_decorator(some_function):

	def wrapper():
		print("Something interesting and important BEFORE some_function() is called.")

		some_function()

		print("Something interesting and important AFTER some_function is called.")

	return wrapper

