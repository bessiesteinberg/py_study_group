# http://pythontutor.com/visualize.html#code=str_a%20%3D%20%22Hello%22%0Astr_b%20%3D%20str_a%0Astr_b%20%2B%3D%20%22%20world!%22%0Aprint%28%22str_a%3A%20%7B%7D%22.format%28str_a%29%29%0Aprint%28%22str_b%3A%20%7B%7D%22.format%28str_b%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
str_a = "Hello"
str_b = str_a
str_b += " world!"
print("str_a: {}".format(str_a))
print("str_b: {}".format(str_b))

# Note: Immutables include:
#  ints
#  floats
#  strings
#  tuples