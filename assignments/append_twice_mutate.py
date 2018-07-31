def append_twice(l, val):
	l.append(val)
	l.append(val)

list_a = [1, 2, 3]
append_twice(list_a, 6)
print(list_a)

# cool it works, but we are mutating the list arg!