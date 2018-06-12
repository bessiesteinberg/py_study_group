from itertools import product, imap

# Find all combos of ABCD and xyz:
a_iter = product(['A','B','C','D'], ['x','y','z'])
print "\nproduct(['A','B','C','D'], ['x','y','z']):"
for i in a_iter:
	print i

# same result:
# b_iter = product('ABCD', 'xyz')
# print "\nproduct('ABCD', 'xyz'):"
# for i in b_iter:
# 	print i

# Find all 2 letter combos of ABCD
# c_iter = product('ABCD', repeat=2)
# for i in c_iter:
# 	print i

# Print it out nicer!
# c_iter = product('ABCD', repeat=2)
# d_iter = imap(''.join, c_iter)
# for i in d_iter:
# 	print i
