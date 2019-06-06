# http://pythontutor.com/visualize.html#code=def%20append_twice%28val,%20l%3D%5B%5D%29%3A%0A%20%20%20%20l.append%28val%29%0A%20%20%20%20l.append%28val%29%0A%20%20%20%20return%20l%0A%0Aprint%28%22append_twice%286%29%3A%20%7B%7D%22.format%28append_twice%286%29%29%29%0Aprint%28%22append_twice%286%29%3A%20%7B%7D%22.format%28append_twice%286%29%29%29%0Aprint%28%22append_twice%286%29%3A%20%7B%7D%22.format%28append_twice%286%29%29%29%0Aprint%28%22append_twice%286%29%3A%20%7B%7D%22.format%28append_twice%286%29%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def append_twice(val, l=[]):
	l.append(val)
	l.append(val)
	return l

print("append_twice(6): {}".format(append_twice(6)))
print("append_twice(6): {}".format(append_twice(6)))
print("append_twice(6): {}".format(append_twice(6)))
print("append_twice(6): {}".format(append_twice(6)))