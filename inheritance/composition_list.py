class Accumulator(object):
	def __init__(self):
		self._container = []
	def accummulate(self, obj):
		self._container.append(obj)
	def stuff(self):
		return self._container[:]

sad_code_base = Accumulator()
sad_code_base.accummulate("tech_debt")
sad_code_base.accummulate("cruft")
sad_code_base.accummulate("no really this is a good idea")
print sad_code_base.stuff()