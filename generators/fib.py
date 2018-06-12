def fib():
	a = 0
	b = 1

	while True:
		next_val = a + b
		a = b
		b = next_val
		yield a



num_times_print = 10
fib_generator = fib()
for i in range(num_times_print):
	print("({}) {}".format(i, fib_generator.next()))


