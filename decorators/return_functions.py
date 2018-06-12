def parent_func(val):

	def child_func_1():
		return "Calling child_func_1()..."

	def child_func_2():
		return "Calling child_func_2()..."

	if val:
		return child_func_1
	else:
		return child_func_2


foo = parent_func(True)
bar = parent_func(False)

print(foo)
print(bar)

print(foo())
print(bar())