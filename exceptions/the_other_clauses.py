while True:
	try:
		print("Let's do some division! Divide 6 by some number:")
		divisor = input()
		ans = 6 / int(divisor)
	except ZeroDivisionError:
		print("Don't divide by zero! Math hates that!")
	except ValueError:
		print("Please enter a number!")
	else:
		print("answer: {}".format(ans))
	finally:
		print("\nLet's do more maths!")
