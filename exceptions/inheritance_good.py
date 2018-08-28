class A(Exception):
	pass

class B(A):
	pass

class C(B):
	pass

for cls in [A, B, C]:
	try:
		raise cls()
	except C:
		print("raised exception C")
	except B:
		print("raised exception B")
	except A:
		print("raised exception A")
		
		