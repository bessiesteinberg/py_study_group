def gen():
	for x in range(5):
		yield x * 2

my_gen = gen()
for n in my_gen:
	print(n)