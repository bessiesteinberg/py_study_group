# visualize: http://pythontutor.com/visualize.html#code=%23%20when%20you%20'change'%20a%20variable%20in%20python%20you%20are%20either%0A%23%20'rebinding'%20it%20or%20'mutating'%20it.%20%20%0A%0A%23%20That%20is%20you%20are%20either%20having%20your%20variable%20stop%20%0A%23%20referencing%20what%20it%20WAS%20referencing%20and%20start%20referencing%0A%23%20something%20new%20%28rebinding%29%3A%0Ax%20%3D%206%0Ax%20%3D%20x%20%2B%201%0A%0A%23%20or%20you%20make%20some%20change%20to%20what%20you%20are%20pointing%20to%20%28mutating%29%3A%0Alist_a%20%3D%20%5B1,%202,%203%5D%0Alist_b%20%3D%20list_a%0Alist_a.append%281%29%0A%0A%23%20Note%3A%20immutables,%20like%20ints,%20cannot%20be%20mutated%20%28well%20named!%29%0A%23%20mutables%20CAN%20be%20rebinded%3A%0Alist_a%20%3D%20%5B4,%205,%206%5D%0Alist_b%20%3D%20list_a%0Alist_a%20%3D%20list_a%20%2B%20%5B1%5D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# when you 'change' a variable in python you are either
# 'rebinding' it or 'mutating' it.  

# That is you are either having your variable stop 
# referencing what it WAS referencing and start referencing
# something new (rebinding):
x = 6
x = x + 1

# or you make some change to what you are pointing to (mutating):
list_a = [3, 1, 4]
list_b = list_a
list_a.append(1)

# Note: immutables, like ints, cannot be mutated (well named!)
# mutables CAN be rebinded:
list_a = [5, 9, 2]
list_b = list_a
list_a = list_a + [6]