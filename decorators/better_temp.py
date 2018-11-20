# What if i want to make it impossible to have a temp <-273*C?
# I could make a setter, but what is to stop a programmer
# from just changing .temp? there are no real private vars in python!
class Celsius(object):
	def __init__(self, temp):
		self.temp = temp

	@property 
	def temp(self):
		return self._temp

	@temp.setter
	def temp(self, temp):
		if temp < -273.15:
			raise Exception("{}C is impossible! No temps < -273.15 allowed!")

		self._temp = temp

	def to_fahrenheit(self):
		return self.temp * 1.8 + 32


temp_0 = Celsius(0)
print(temp_0.to_fahrenheit())
temp_40 = Celsius(40)
print(temp_40.to_fahrenheit())


# temp_very_low = Celsius(-300)
# print(temp_very_low.to_fahrenheit())

temp_0.temp -= 300