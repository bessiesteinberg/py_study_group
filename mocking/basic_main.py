import time

class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

	def volume(self, height=0):
		"""
		returns volume of this rectangle if it had 
		the given height
		... this is obviously a very compicated 
		calculation that takes a long time
		"""
		time.sleep(5)
		return self.area() * height