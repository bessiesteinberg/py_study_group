def divide_by_zero(val):
	return val / 0

try:
	print("Let's do some division!")
	x = divide_by_zero(6)
	print("x: {}".format(x))
except ZeroDivisionError:
	print("You can't divide by zero! YOU BROKE MATH!!")