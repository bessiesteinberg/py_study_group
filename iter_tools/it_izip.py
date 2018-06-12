import itertools

list_a = ['twas', 'brillig', 'and', 'the', 'slithy', 'toves']
list_b = [3, 1, 4, 5, 6, 9]

zipped = itertools.izip(list_a, list_b)

for i in zipped:
	print i