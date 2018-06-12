def mults_of_2():
	counter = 1
	while True:
		yield counter * 2
		counter += 1


num_times_print = 10
mults2_generator = mults_of_2()
for i in range(num_times_print):
	print("({}) {}".format(i, mults2_generator.next()))