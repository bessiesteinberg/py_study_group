class Accumulator(object):
	def __init__(self):
		self._container = []

	def accummulate(self, obj):
		self._container.append(obj)

	def stuff(self):
		return self._container[:]

	def contains(self, item):
		return item in self._container


hamilton = Accumulator()

hamilton.accummulate("power")
hamilton.accummulate("debt")
print("hamilton.stuff(): {}".format( hamilton.stuff() ))

print("\nhamilton.contains(\"ounce of regret\"): {}".format(
	hamilton.contains("ounce of regret")
))

print()


