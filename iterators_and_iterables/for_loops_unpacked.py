def unpacked_foor_loop(iterable):
	# does the same thing as:
	# for i in iter_obj:
	#	print(i)

	iter_obj = iter(iterable)

	while True:
		try:
			i = next(iter_obj)
			print(i)
		except StopIteration:
			break

# lists
print("~~~ Lists: ~~~")
unpacked_foor_loop(['hello', 'world', 3, 1, 4])

# generators
print("~~~ Generators: ~~~")
unpacked_foor_loop(range(10))

# strings
print("~~~ Strings: ~~~")
unpacked_foor_loop('hello world')

# files
print("~~~ Files: ~~~")
with open('example.txt') as f:
	unpacked_foor_loop(f)