def mults_of_2_with_max(max_counter):
	counter = 1
	while counter <= max_counter:
		yield counter * 2
		counter += 1


# num_times_print = 10
# mults2_generator = mults_of_2_with_max(6)
# for i in range(num_times_print):
# 	print("({}) {}".format(i, mults2_generator.next()))


# PYTHON SAD! Try this instead!
mults2_generator = mults_of_2_with_max(6)
for val in mults2_generator:
	print("> {}".format(val))

