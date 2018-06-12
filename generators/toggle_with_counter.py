def toggle():
	# Return true the first time called, then false, then true...
	counter = 0
	while True:
		if (counter % 2) == 0:
			yield True
		else:
			yield False

		counter += 1

num_times_print = 10
toggle_gen = toggle()
for i in range(num_times_print):
	print("({}) {}".format(i, toggle_gen.next()))