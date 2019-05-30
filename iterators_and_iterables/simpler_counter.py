def counter(low, high):
	current = low
	while current <= high:
		yield current
		current += 1

for i in counter(3, 5):
	print(i)