import sys

# you can mess with sys.path (you probs shouldn't though)
sys.path = ['']

from cactus import say_hello
say_hello()

from five import Five
f = Five()
print(f())
print(f.loud())
