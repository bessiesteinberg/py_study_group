squared_evens = (e*e for e in (x for x in range(20) if (x % 2 == 0)))

for squared_even in squared_evens:
	print(squared_even)