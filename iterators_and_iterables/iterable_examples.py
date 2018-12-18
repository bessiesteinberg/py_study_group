# lists
print("~~~ Lists: ~~~")
for i in ['hello', 'world', 3, 1, 4]:
	print(i)

# generators
print("~~~ Generators: ~~~")
for i in range(10):
	print(i)

# strings
print("~~~ Strings: ~~~")
for i in 'hello world':
	print(i)

# files
print("~~~ Files: ~~~")
with open('example.txt') as f:
	for i in f:
		print(i)
