from random import randint
# Let's create an iterable that produces unique random ints in a range until
# it generates a random number it has already generated

class UniqueRandInt(object):
	def __init__(self, low, high):
		self.low = low
		self.high = high
		self.values = set()

	def __iter__(self):
		while True:
			current = randint(self.low, self.high)
			
			if current in self.values:
				raise StopIteration

			yield current

			self.values.add(current)

for i in UniqueRandInt(1, 5):
	print(i)
