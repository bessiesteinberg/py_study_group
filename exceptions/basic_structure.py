try:
	print("Let's do some division!")
	x = 6 / 0
	print("x: {}".format(x))
except ZeroDivisionError:
	print("You can't divide by zero! YOU BROKE MATH!!")