import six
my_gen = (x for x in range(10))

# works for python 2
print(my_gen.next())

# works for python 2.5+ including python 3
print(next(my_gen))

# works for python 2 and 3
print(six.advance_iterator(my_gen))