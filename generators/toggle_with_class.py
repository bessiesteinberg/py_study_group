def toggle():
	while True:
		yield True
		yield False


toggle_gen = toggle()
for i in range(10):
	print(toggle_gen.next())