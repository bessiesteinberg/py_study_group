def fizz_buzz():
	counter = 0
	while True:
		str = ''
		if (counter % 3) == 0:
			str += 'fizz'

		if (counter % 5) == 0:
			str += 'buzz'

		yield str
		counter += 1

num_times_print = 20
fizz_buzz_generator = fizz_buzz()
for i in range(num_times_print):
	print("({}) {}".format(i, fizz_buzz_generator.next()))