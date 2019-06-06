# visualize: http://pythontutor.com/visualize.html#code=%23%20You%20can%20have%20references%20that%20aren't%20names%3A%0Ax%20%3D%20%5B1,%202,%203%5D%0Alist_a%20%3D%20%5B%22hello%22,%20x,%20%22world%22%5D%0Adict_b%20%3D%20%7B%0A%20%20%20%20%22key_a%22%3A%206,%0A%20%20%20%20%22key_b%22%3A%20x%0A%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# You can have references that aren't names:
x = [1, 2, 3]
list_a = ["hello", x, "world"]
dict_b = {
	"key_a": 6,
	"key_b": x
}

print("x: {}".format(x))
print("list_a[1]: {}".format(list_a[1]))
print("dict_b['key_b']: {}".format(dict_b['key_b']))

# this is to illustrate 2 points:
# (1) references don't have to be 'names'
# (2) you gotta be careful how you pass around and change 
#	mutable values
