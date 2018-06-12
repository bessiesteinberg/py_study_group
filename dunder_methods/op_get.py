class Length(object):

    metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
               "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
               "mi" : 1609.344 }

    def __init__(self, value, unit="m"):
    	self.value = value
    	self.unit = unit

    def Convert2Meters(self):
    	return self.value * Length.metric[self.unit]

    def Convert2NewUnit(self, new_unit):
        return self.Convert2Meters() / Length.metric[new_unit]

    def __add__(self, other):
    	l = self.Convert2Meters() + other.Convert2Meters()
    	return Length(l/Length.metric[self.unit], self.unit)

    def __sub__(self, other):
    	l = self.Convert2Meters() - other.Convert2Meters()
    	return Length(l/Length.metric[self.unit], self.unit)

    def __getitem__(self, new_unit):
        """ return the value converted into the given unit """
        return self.Convert2NewUnit(new_unit)


a = Length(42, "mm")
print("a['cm']: {}".format(a['cm']))
print("a['m']: {}".format(a['m']))
print("a['km']: {}".format(a['km']))
print("a['mi']: {}".format(a['mi']))

