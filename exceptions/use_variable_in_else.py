my_list = ['hello', 'world']
try:
	something = my_list[1]
except IndexError:
	print("ERROR!")
else:
	# MANY LINES OF CODE
	print(something)