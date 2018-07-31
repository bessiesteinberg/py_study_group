# visualize: http://pythontutor.com/visualize.html#code=def%20some_func%28val%29%3A%0A%20%20%20%20print%28%22from%20some_func%3A%20val%3A%20%7B%7D%22.format%28val%29%29%0A%0Ax%20%3D%20%5B1,%202,%203%5D%0Asome_func%28x%29&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def some_func(val):
    print("from some_func: val: {}".format(val))

x = [1, 2, 3]
some_func(x)

# NOTE: 
# (1) val and x are references to the same value
# (2) val is NOT a reference to x
# (3) val isn't a copy of x there are the same thing