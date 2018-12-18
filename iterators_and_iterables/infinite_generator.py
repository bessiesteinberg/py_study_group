def toggle():
	while True:
		yield True
		yield False

for i in toggle():
	print(i)