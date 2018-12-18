# example credit: https://stackoverflow.com/questions/19151/build-a-basic-python-iterator

class Counter(object):
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		# import pudb; pudb.set_trace()
		return self

	def __next__(self):
		# import pudb; pudb.set_trace()
		if self.current > self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.current - 1

for c in Counter(3, 5):
	print(c)