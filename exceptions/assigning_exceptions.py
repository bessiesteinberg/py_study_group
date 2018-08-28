try:
	print("Let's do some division!")
	x = 6 / 0
	print("x: {}".format(x))
except ZeroDivisionError as e:
	print(e)