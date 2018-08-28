my_list = ['hello', 'world']
something = None
try:
	something = my_list[1]
except IndexError:
	print("ERROR!")

# MANY LINES OF CODE
if something is not None:
# if 'something' in locals():
	print(something)