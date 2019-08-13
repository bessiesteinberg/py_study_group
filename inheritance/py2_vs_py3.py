class A(object):
	def __init__(self):
		super().__init__()
		# super(__class__, self).__init__()
		print("init A")

class B(A):
	def __init__(self):
		super().__init__()
		# super(__class__, self).__init__()
		print("init B")

class C(B):
	def __init__(self):
		import pudb; pudb.set_trace()
		super().__init__()
		# super(__class__, self).__init__()
		print("init C")


c = C()