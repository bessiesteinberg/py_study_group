# Bound Methods: are methods that are tied to / associated with an
# 	an instance of a class

class UpperCase(object):
	def __init__(self, name=None):
		if name:
			self.my_fav_name = name
		else:
			self.my_fav_name = "Bessie"

	def bound(self): # note that the arg 'self'
		return self.my_fav_name.upper()

	@staticmethod
	def unbound(s):
		return s.upper()

def someFunc(c): 
	# arg c: some callable
	return c("decoris deformi melior est")

bessie = UpperCase()
chris = UpperCase("Chris")

print(bessie.bound())
print(UpperCase.bound(bessie))
print(UpperCase.bound(chris))



# inst_of_upper_case = UpperCase()
# print(UpperCase.bound("Chris", "decoris deformi melior est"))

# print(inst_of_upper_case.unbound("decoris deformi melior est"))
# print(UpperCase.unbound("decoris deformi melior est"))



# print("someFunc(inst_of_upper_case.bound): {}".format( someFunc(inst_of_upper_case.bound) ))
# print("someFunc(UpperCase.bound): {}".format( someFunc(UpperCase.bound) ))

# # print("someFunc(inst_of_upper_case.unbound): {}".format( someFunc(inst_of_upper_case.unbound) ))
# # print("someFunc(UpperCase.unbound): {}".format( someFunc(UpperCase.unbound) ))
