def append_length_to_str(s):
	length_of_s = len(s)
	return s + " (" + str(length_of_s) + ")"

# create generator exp 1...10
num = (x for x in range(1, 11))
# for every line print one more turtle
turtles = ('turtle'*x for x in num)
# replace instances of double turtle (turtleturtle) with turtledove
turtledoves = (s.replace("turtleturtle", "turtledove") for s in turtles)
# print length at the end of each line
turtledove_lens = (append_length_to_str(s) for s in turtledoves)

for s in turtledove_lens:
	print(s)


