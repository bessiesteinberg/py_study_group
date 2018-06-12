import itertools

list_a = ['twas', 'brillig', 'and', 'the', 'slithy', 'toves']
list_b = [3, 1, 4, 5, 6, 9]

chained = itertools.chain(list_a, list_b)
print chained

# for i in chained:
# 	print i

# print list(chained)