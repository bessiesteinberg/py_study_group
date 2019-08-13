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


class B(A):
	def __init__(self):
		super(B, self).__init__()
		print("init B")

	important_value = "B"

class C(A):
	def __init__(self):
		super(C, self).__init__()
		print("init C")

	important_value = "C"

class D(B,C):
	def __init__(self):
		super(D, self).__init__()
		print("init D")

class E(C,B):
	def __init__(self):
		super(E, self).__init__()
		print("init E")

	

print("\nd=D()...")
d=D()
print("D.important_value: " + D.important_value)

# print("\ne=E()...")
# e=E()
# print("E.important_value: " + E.important_value)

# print()
