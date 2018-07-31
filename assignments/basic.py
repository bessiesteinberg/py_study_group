x = 42
# x -> 42
y = x
# x -> 42
# y ---^
x = 6
#      42
# y ---^
# x -> 6

# Note: there is no assigning name to name
# in line 3, y is not a reference to x
# x and y are both a reference to 42
