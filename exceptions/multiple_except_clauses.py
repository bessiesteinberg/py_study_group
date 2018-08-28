while True:
	try:
		print("Let's do some division! Divide 6 by some number:")
		divisor = input()
		ans = 6 / int(divisor)
		print("answer: {}".format(ans))
	except ZeroDivisionError:
		print("Don't divide by zero! Math hates that!")
	except ValueError:
		print("Please enter a number!")