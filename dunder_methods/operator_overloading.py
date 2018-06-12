class Length(object):

    metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
               "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
               "mi" : 1609.344 }

    def __init__(self, value, unit="m"):
    	self.value = value
    	self.unit = unit

    def Convert2Meters(self):
    	return self.value * Length.metric[self.unit]

    def __add__(self, other):
    	l = self.Convert2Meters() + other.Convert2Meters()
    	return Length(l/Length.metric[self.unit], self.unit)

    def __sub__(self, other):
    	l = self.Convert2Meters() - other.Convert2Meters()
    	return Length(l/Length.metric[self.unit], self.unit)


a = Length(42, "mm")
print("a: {} {}".format(a.value, a.unit))
b = Length(6)
print("b: {} {}".format(b.value, b.unit))
c = a+b
print("a + b: {} {}".format(c.value, c.unit))
d = a - b
print("a - b: {} {}".format(d.value, d.unit))