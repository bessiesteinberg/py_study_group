class A(Exception):
	pass

class B(A):
	pass

class C(B):
	pass

for cls in [A, B, C]:
	try:
		raise cls()
	except A as e:
		print(type(e))
		
		print("raised exception A")
	except B:
		print("raised exception B")
	except C:
		print("raised exception C")
		
		