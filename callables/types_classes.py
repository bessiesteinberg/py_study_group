class OtherClass(object):
	pass

print( callable(OtherClass) )
print( dir(OtherClass))

class SomeClass(object):
	def __init__(val):
		self.val = val

print( callable(SomeClass ) )
