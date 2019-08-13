class Tea(object):
	def __init__(self, caffine_level, deliciousness):
		self.caffine_level = caffine_level
		self.deliciousness = deliciousness

	def is_caffine_free(self):
		return self.caffine_level == 0

	def is_delicious_enough(delicious_threshold=3):
		return self.deliciousness >= delicious_threshold

# Inheritance:
class Oolong(Tea):
	def __init__(self):
		super(Oolong, self).__init__(caffine_level=4, deliciousness=10)


# Composition:
class Rooibos(object):
	def __init__(self):
		self.tea = Tea(caffine_level=0, deliciousness=2)


oolong = Oolong()
print("\nIs oolong caffine free? {}".format(
		oolong.is_caffine_free()
	))

rooibos = Rooibos()
print("\nIs rooibos caffine free? {}".format(
		rooibos.tea.is_caffine_free()
	))

