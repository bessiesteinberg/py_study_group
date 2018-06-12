from itertools import count, islice, tee

##
# iterators are cool, but its a bummer that you can only use 
# once
orig_iter = islice(count(), 10)
for i in orig_iter:
	print i

# print "orig_iter.next():"
# orig_iter.next()

##
# tee lets you make multiple iterators from the same original!
# orig_iter = islice(count(), 10)
# i1, i2 = tee(orig_iter)
# print "\ni1:"
# for i in i1:
# 	print i

# print "\ni2:"
# for i in i2:
# 	print i

##
# Careful! they are starting from the same original
# orig_iter = islice(count(), 10)
# i1, i2 = tee(orig_iter)

# print "\n orig_iter"
# print "orig_iter.next()"
# print orig_iter.next()
# print "orig_iter.next()"
# print orig_iter.next()

# print "\ni1:"
# for i in i1:
# 	print i

# print "\ni2:"
# for i in i2:
# 	print i