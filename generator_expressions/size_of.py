from sys import getsizeof

l = [x*2 for x in range(5)]
print( getsizeof( l ) )

g = (x*2 for x in range(5))
print( getsizeof( g ) )

l = [x*2 for x in range(10000)]
print( getsizeof( l ) )

g = (x*2 for x in range(10000))
print( getsizeof( g ) )