import sys
# You can just have a general exception that will catch everything
# This is generally bad pracitice as it may hide important errors
# You may want to log the error and re-raise it

while True:
	try:
		print("Let's do some division! Divide 6 by some number:")
		divisor = input()
		ans = 6 / int(divisor)
		print("answer: {}".format(ans))
	except ZeroDivisionError:
		print("Don't divide by zero! Math hates that!")
	except Exception as e:
		print("Unexpected error:", sys.exc_info()[0])
		raise e
