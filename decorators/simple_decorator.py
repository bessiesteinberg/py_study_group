def simple_decorator(some_func):

	def wrapper():
		print("About to call some_func!!!!")

		some_func()

		print("some_func was just called!!")

	return wrapper


def boring_function():
	print("hey!")

decorated_function = simple_decorator(boring_function)

decorated_function()

print("\n\n\n")

def different_function():
	print("I'm  a different_function!!")

different_function = simple_decorator(different_function)
different_function()