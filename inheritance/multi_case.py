class A(object):
	def some_method(self):
		return "some_method: A"

class B(object):
	def other_method(self):
		return "other_method: B"

class C(A,B):
	pass

c = C()
print "c.some_method: {}".format(c.some_method())
print "c.other_method: {}".format(c.other_method())
