# visualize: http://pythontutor.com/visualize.html#code=def%20some_func%28val%29%3A%0A%20%20%20%20print%28%22from%20some_func%3A%20val%3A%20%7B%7D%22.format%28val%29%29%0A%0Ax%20%3D%2042%0Asome_func%28x%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# there are several interesting kinds of assignment in 
# this simple file

# the name 'some_func' becomes the reference to this 
# function object
def some_func(val):
	# the argument 'val' becomes a reference 
	print("from some_func: val: {}".format(val))

# regular assignment we are accustomed to
x = 42
some_func(x)
