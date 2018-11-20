class Celsius(object):
	def __init__(self, temp):
		self.temp = temp

	def to_fahrenheit(self):
		return self.temp * 1.8 + 32


temp_0 = Celsius(0)
print(temp_0.to_fahrenheit())
temp_40 = Celsius(40)
print(temp_40.to_fahrenheit())
temp_very_low = Celsius(-300)
print(temp_very_low.to_fahrenheit())
	