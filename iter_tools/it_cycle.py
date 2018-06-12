import itertools

sequence = ['all', 'mimsy', 'were', 'the', 'borogroves']
a_cycle = itertools.cycle(sequence)

for i in xrange(20):
	print a_cycle.next()