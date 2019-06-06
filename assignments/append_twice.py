def append_twice(l, val):
	l = l + [val, val]
	return l

list_a = [1, 2, 3]
list_b = append_twice(list_a, 6)
print(list_a)
print(list_b)
