from unittest.mock import MagicMock

class Rectangle3D(object):
	def __init__(self, length=5, width=10, height=6):
		self.length = length
		self.width = width
		self.height = height

	def area(self):
		print("area called")
		return self.length * self.width

	def volume(self):
		print("volume called")
		return self.area() * self.height

	def mass(self, density=1):
		print("mass called")
		return self.volume() * density

	def weight(self, gravitational_acceleration=9.8, density=None):
		print("weight called")
		if density:
			mass = self.mass(density)
		else:
			mass = self.mass()

		return mass * gravitational_acceleration


real = Rectangle3D()
real.mass = MagicMock()
import pdb; pdb.set_trace()
w = real.weight()
real.mass.assert_called_once()
print("weight: {}".format(w))
print("call count: {}".format(real.mass.call_count))
print("call_args_list: {}".format(real.mass.call_args_list))

print("---------")
real.weight(density=2)
# import pdb; pdb.set_trace()
real.mass.assert_called_with(2)
print("call count: {}".format(real.mass.call_count))
print("call_args_list: {}".format(real.mass.call_args_list))
# import pdb; pdb.set_trace()

print("---------")
real.mass.return_value = 10
w = real.weight()
print("weight: {}".format(w))
print("call count: {}".format(real.mass.call_count))
print("call_args_list: {}".format(real.mass.call_args_list))

