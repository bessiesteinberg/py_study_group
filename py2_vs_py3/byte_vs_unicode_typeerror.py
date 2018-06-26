# Python 2 is **generally** okay with converting between 
# unicode and bytes, python 3 will not let you and will through
# a TypeError
s = "Hello "
print("string s: value: {}, type: {}".format(s, type(s)))
b = b'World'
print("byte string b: value {}, type: {}".format(b, type(b)))

hw = s + b
print("s + b: {}".format(hw))