from itertools import compress, cycle

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
bools = [True, True, False, True, True, False, True]

# compress returns an iterator.  It only returns values in
# the first list if the corresponding value in the second 
# list is true

for i in compress(alphabet, bools):
	print i

# itnerestingly, it doesn't have to be bools it could be ints
# ints = [1, 0, 0, 2, 0, 0, 3]
# for i in compress(alphabet, ints):
# 	print i


# lets say i only want every other value from alphabet
# i could ...
# bools = [True, False, True, False, True, False, True]
# for i in compress(alphabet, bools):
# 	print i

# but since compress will terinate on the shortest input i 
# could have one of these be an infinite iterator
# for i in compress(alphabet, cycle([True, False])):
# 	print i