import itertools

list_a = ['twas', 'brillig', 'and', 'the', 'slithy', 'toves']

zipped = itertools.izip(itertools.count(), list_a)

for i in zipped:
	print i