evens = (x for x in range(20) if (x % 2 == 0))
squared_evens = (e*e for e in evens)

for squared_even in squared_evens:
	print(squared_even)