# take all evens < 20 and square them
squared_evens = (e*e for e in range(20) if (e % 2 == 0))

for squared_even in squared_evens:
	print(squared_even)
	