class A(object):
	def some_method(self):
		return "some_method: A"

	def other_method(self):
		return "other_method: A"

class B(object):
	def __init__(self):
		self.a = A()

	def some_method(self):
		return "some_method: B"

	def other_method(self):
		return self.a.other_method()

a = A()
b = B()
print "a.some_method: {}".format(a.some_method())
print "b.some_method: {}".format(b.some_method())
print "a.other_method: {}".format(a.other_method())
print "b.other_method: {}".format(b.other_method())
