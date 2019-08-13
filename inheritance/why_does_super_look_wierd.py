"""
  A       
 / \     
B   C   
 \ /    
  D     
"""

class A(object):
	def weird_method(self):
		print("weird_method: A")

	def normal_method(self):
		print("normal_method: A")



class B(A):
	def weird_method(self):
		super(B, self).weird_method()
		print("weird_method: B")

	def normal_method(self):
		super(B, self).normal_method()
		print("normal_method: B")



class C(A):
	def weird_method(self):
		super(C, self).weird_method()
		print("weird_method: C")

	def normal_method(self):
		super(C, self).normal_method()
		print("normal_method: C")


class D(B,C):
	def weird_method(self, some_class):
		# NOTE: using super improperly!
		import pudb; pudb.set_trace()
		super(some_class, self).weird_method()
		print("weird_method: D")

	def normal_method(self):
		super(D, self).normal_method()
		print("normal_method: D")

class E(C,B):
	def weird_method(self, some_class):
		# NOTE: using super improperly!
		import pudb; pudb.set_trace()
		super(some_class, self).weird_method()
		print("weird_method: D")

	def normal_method(self):
		super(D, self).normal_method()
		print("normal_method: D")	


print("B MRO: {}".format(B.__mro__))
print("D MRO: {}".format(D.__mro__))

d = D()
e = E()

d.normal_method()

# d.weird_method(D)
# d.weird_method(B)
# e.weird_method(B)
# d.weird_method(A)
# d.weird_method(E)


