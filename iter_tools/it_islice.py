from itertools import islice, count

print "Stop at 6"
for i in islice(count(), 6):
	print i

print "Start at 6, Stop at 12"
for i in islice(count(), 6, 12):
	print i

print "Start at 0, Stop at 12, in Steps of 3"
for i in islice(count(), 0, 12, 3):
	print i