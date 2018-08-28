while True:
	try:
		print("Let's do some division! Divide 6 by some number:")
		divisor = input()
		ans = 6 / int(divisor)
		print("answer: {}".format(ans))
	except (ZeroDivisionError, ValueError) as e:
		print(e)