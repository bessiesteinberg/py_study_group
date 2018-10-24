# format: map(callable, iteratable)

some_list = [1,1,2,3,5,8,13,21,34]

# def add_2(val):
# 	return val + 2

# map_add_2 = map(add_2, some_list)
# for i in map_add_2:
# 	print(i)

# map_add_2 = map(lambda x: x+2, some_list)
# for i in map_add_2:
# 	print(i)

class AddTwo(object):
	def __init__(self, val):
		self.val = val + 2

	def __str__(self):
		return "AddTwo({})".format(self.val)

map_add_2 = map(AddTwo, some_list)
for i in map_add_2:
	print(i)