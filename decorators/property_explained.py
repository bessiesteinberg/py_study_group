class Celsius(object):
	def __init__(self, temp):
		self.temp = temp

	def temp_getter(self):
		return self._temp

	def temp_setter(self, temp):
		if temp < -273.15:
			raise Exception("{}C is impossible! No temps < -273.15 allowed!")

		self._temp = temp
	
	temp = property(temp_getter)
	print(temp)
	temp = temp.setter(temp_setter)


	def to_fahrenheit(self):
		return self.temp * 1.8 + 32


t = Celsius(60)
