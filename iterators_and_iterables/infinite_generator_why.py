def toggle():
	while True:
		yield True
		yield False

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


unpacked_foor_loop(toggle())