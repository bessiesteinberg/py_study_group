# lambdas: lamdas are one line functions
# format: lambda arg: do_stuff_to(arg)

add_2 = lambda x: x + 2
print("add_2(5): {}".format( add_2(5) ))

# they can take more then one arg
add = lambda x, y: x + y
print("add(5,4): {}".format( add(5,4) ))

# they can call other callables
add_4 = lambda x: add_2(add_2(x)) # yes this is def the best way to do this
print("add_4(5): {}".format( add_4(5) ))

append_len_to_str = lambda x: x + str(len(x))
print("append_len_to_str('string'): {}".format(append_len_to_str('string')))

print()
print("Is add_2() callable?: {}".format( callable(add_2) ))
print("Is add() callable?: {}".format( callable(add) ))
print("Is add_4() callable?: {}".format( callable(add_4) ))
print("Is append_len_to_str() callable?: {}".format( callable(append_len_to_str) ))