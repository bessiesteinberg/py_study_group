my_list = ['hello', 'world']
try:
	something = my_list[1]
	# MANY LINES OF CODE
	print(something)
except IndexError:
	print("ERROR!")