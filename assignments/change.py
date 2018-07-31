# visualize: https://goo.gl/XCn6oX

# when you 'change' a variable in python you are either
# 'rebinding' it or 'mutating' it.  

# That is you are either having your variable stop 
# referencing what it WAS referencing and start referencing
# something new (rebinding):
x = 6
x = x + 1

# or you make some change to what you are pointing to (mutating):
list_a = [1, 2, 3]
list_b = list_a
list_a.append(1)

# Note: immutables, like ints, cannot be mutated (well named!)
# mutables CAN be rebinded:
list_a = [4, 5, 6]
list_b = list_a
list_a = list_a + [1]