import itertools

def fib():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b
		
fib_val = fib()

for val in itertools.islice(fib_val, 10):
	print(val)

print('next')

for val in itertools.islice(fib_val, 10):
	print(val)