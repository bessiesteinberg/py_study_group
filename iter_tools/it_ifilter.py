from itertools import ifilter, ifilterfalse

a_iter = ifilter(lambda x: ((x % 3) == 0), xrange(20)) 
for i in a_iter:
	print i

# b_iter = ifilterfalse(lambda x: ((x % 3) == 0), xrange(20))
# for i in b_iter:
# 	print i


# advice = ["beware", "the", "jubjub", "bird", "and", "shun", "the", "frumious", "bandersnatch"]
# real_words = ["beware", "the", "bird", "and", "shun"]

# fake_words = ifilterfalse(lambda word: word in real_words, advice)
# for word in fake_words:
# 	print word