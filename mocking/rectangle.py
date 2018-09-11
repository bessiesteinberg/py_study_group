class Rectangle3D(object):
	def __init__(self, length=5, width=10, height=6):
		self.length = length
		self.width = width
		self.height = height

	def area(self):
		# print("area called")
		return self.length * self.width

	def volume(self):
		# print("volume called")
		return self.area() * self.height

	def mass(self, density=1):
		# print("mass called")
		return self.volume() * density

	def weight(self, gravitational_acceleration=9.8, density=None):
		# print("weight called")
		if density:
			mass = self.mass(density)
		else:
			mass = self.mass()

		return mass * gravitational_acceleration


def weight_of_cube(edge_len=1):
	rect3D = Rectangle3D(length=edge_len, width=edge_len, height=edge_len)
	return rect3D.weight()