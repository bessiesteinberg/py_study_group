class A(object):
	def some_method(self):
		print("some_method: A")

class B(A):
	def some_method(self):
		super(B, self).some_method()
		print("some_method: B")

class C(B):
	pass

c = C()
print("\nc.some_method():")
c.some_method()

print()
