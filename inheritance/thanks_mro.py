"""
  A       A
 / \     / \
B   C   C   B
 \ /     \ /
  D       E
"""

class A(object):
	def __init__(self):
		print("init A")

	def somemethod(self):
		print("some_method - A")

	x = "A"

class B(A):
	def __init__(self):
		super(B, self).__init__()
		print("init B")

	important_value = "B"
	def somemethod(self):
		super(B, self).somemethod()
		print("some_method - B")

class C(A):
	def __init__(self):
		super(C, self).__init__()
		print("init C")

	important_value = "C"
	def somemethod(self):
		super(C, self).somemethod()
		print("some_method - C")

class D(B,C):
	def __init__(self):
		super(D, self).__init__()
		print("init D")

class E(C, B):
	def __init__(self):
		super(E, self).__init__()
		print("init E")

	

print("D.mro: {}".format( D.__mro__ ))
print("E.mro: {}".format( E.__mro__ ))
# print("C.mro: {}".format( C.__mro__ ))
# print("B.mro: {}".format( B.__mro__ ))

print("\nd=D()...")
d=D()
d.somemethod()

print("D.important_value: " + D.important_value)
print()

print("\ne=E()...")
e=E()
e.somemethod()
print("E.important_value: " + E.important_value)
print()


