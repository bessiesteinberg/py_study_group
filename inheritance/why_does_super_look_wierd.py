"""
  A       
 / \     
B   C   
 \ /    
  D     
"""

class A(object):
	def __init__(self):
		print "init A"

	def normal_method(self):
		print "normal_method: A"
		print "type(self) {}".format(type(self))



class B(A):
	def __init__(self):
		super(B, self).__init__()
		print "init B"

	def normal_method(self):
		super(B, self).normal_method()
		print "normal_method: B"
		print "type(self) {}".format(type(self))



class C(A):
	def __init__(self):
		super(C, self).__init__()
		print "init C"

	def normal_method(self):
		super(C, self).normal_method()
		print "normal_method: C"
		print "type(self) {}".format(type(self))



class D(B,C):
	def __init__(self):
		# NOTE: using super improperly!
		super(B, self).__init__()
		print "init D"

	def normal_method(self):
		super(D, self).normal_method()
		print "normal_method: D"
		print "type(self) {}".format(type(self))


print("B MRO: {}".format(B.__mro__))
print("D MRO: {}".format(D.__mro__))

d = D()

d.normal_method()


