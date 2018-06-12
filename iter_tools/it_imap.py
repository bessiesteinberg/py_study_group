from itertools import imap

list_a = [2,4,6,8]
list_b = [1,2,3,4]

mapped = imap(pow, list_a, list_b)
for i in mapped:
	print i

# no function
mapped = imap(None, list_a, list_b)
for i in mapped:
	print i