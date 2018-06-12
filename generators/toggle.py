def toggle():
	# Return true the first time called, then false, then true...
	while True:
		yield True
		yield False

num_times_print = 10
toggle_gen = toggle()
for i in range(num_times_print):
	print("({}) {}".format(i, toggle_gen.next()))