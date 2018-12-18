class Counter(object):
	def __init__(self, low, high):
		self.low = low
		self.high = high

	def __iter__(self):
		# import pudb; pudb.set_trace()
		current = self.low
		while current <= self.high:
			yield current
			current += 1

for c in Counter(3, 5):
	print(c)