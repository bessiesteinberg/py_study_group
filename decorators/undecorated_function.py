def my_function():
	""" Very Informative Docstring """
	print("Calling function")

my_function()
print("my_function name: {}".format(my_function.__name__))
print("my_function doc: {}".format(my_function.__doc__))