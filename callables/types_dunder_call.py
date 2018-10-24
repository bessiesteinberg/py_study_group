class MultStuff(object):
	def __init__(self, multiplier):
		self.multiplier = multiplier

	def __call__(self, val):
		return self.multiplier * val

mult2 = MultStuff(2)
print("mult2(10): {}".format( mult2(10) ))
mult5 = MultStuff(5)
print("mult5(10): {}".format( mult5(10) ))

print("Is MultStuff() callable? {}".format( callable(MultStuff) ))
print("Is mult2() callable? {}".format( callable(mult2) ))
print("Is mult5() callable? {}".format( callable(mult5) ))