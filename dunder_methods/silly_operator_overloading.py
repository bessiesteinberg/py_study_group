class B(object):
	def __init__(self, value):
		self.value = value

	def __mul__(self, other):
		return r'(\/)!_!(\/)'



b1 = B(1)
b2 = B(2)
b3 = b1 * b2
print(b3)