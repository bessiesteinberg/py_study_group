"""
  A       A
 / \     / \
B   C   C   B
 \ /     \ /
  D       E
"""

class A(object):
	def __init__(self):
		print "init A"

	def some_method(self):
		print "some_method - A"

	x = "A"

class B(A):
	def __init__(self):
		super(B, self).__init__()
		print "init B"

	name = "B"

class C(A):
	def __init__(self):
		super(C, self).__init__()
		print "init C"

	name = "C"

class D(B,C):
	def __init__(self):
		super(D, self).__init__()
		print "init D"

class E(C, B):
	def __init__(self):
		super(E, self).__init__()
		print "init E"

	

print("D.mro: {}".format( D.__mro__ ))
print("E.mro: {}".format( E.__mro__ ))
print("C.mro: {}".format( C.__mro__ ))
print("B.mro: {}".format( B.__mro__ ))

print("d=D()...")
d=D()
print("D.name: " + D.name)

print("e=E()...")
e=E()
print("E.name: " + E.name)

print("b=B()...")
b=B()

