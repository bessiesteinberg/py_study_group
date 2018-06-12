from itertools import product, permutations, combinations, combinations_with_replacement, imap

prod = imap(''.join, product('ABCD', repeat=2))
print("product: {}".format(list(prod)))

perm = imap(''.join, permutations('ABCD', 2))
print("permutations: {}".format(list(perm)))

comb = imap(''.join, combinations('ABCD', 2))
print("combinations: {}".format(list(comb)))

combwr = imap(''.join, combinations_with_replacement('ABCD', 2))
print("com with replacement: {}".format(list(combwr)))
