import itertools

a_count = itertools.count()
while True:
	i = a_count.next()
	print i
	if i >= 10:
		break

# b_count = itertools.count(6)
# while True:
# 	i = b_count.next()
# 	print i
# 	if i >= 10:
# 		break

# c_count = itertools.count(6, 3)
# while True:
# 	i = c_count.next()
# 	print i
# 	if i >=30:
# 		break