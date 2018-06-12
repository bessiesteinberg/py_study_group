import itertools

a_iter = itertools.repeat(20)

for i in xrange(15):
	print a_iter.next()

# b_iter = itertools.repeat(20, 15)
# for i in b_iter:
# 	print i