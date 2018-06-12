from functools import wraps
def my_decorator(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		print("Calling decorated function")
		return f(*args, **kwargs)
	# wrapper = wraps(f)(wrapper)
	return wrapper

@my_decorator
def my_function():
	""" Very Informative Docstring """
	print("Calling function")

my_function()
print("my_function name: {}".format(my_function.__name__))
print("my_function doc: {}".format(my_function.__doc__))