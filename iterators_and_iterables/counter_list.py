# Counter is the iterable, it implements __iter__ 
class Counter(object):
	def __init__(self, low, high):
		self.values = [x for x in range(low, high+1)]

	def __iter__(self):
		return ListIterator(self.values)

# List Iterator is the iterator it implements __next__
class ListIterator(object):
	def __init__(self, my_list):
		self.list = my_list
		self.index = 0
		self.length = len(my_list)

	def __next__(self):
		if self.index >= self.length:
			raise StopIteration

		curr_value = self.list[self.index]
		self.index += 1
		return curr_value

for c in Counter(3, 5):
	print(c)

