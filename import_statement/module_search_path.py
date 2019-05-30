# 1. search in builtins:


# 2. look in sys.path
import sys
print(f"sys.path: {sys.path}")

from cactus import say_hello
say_hello()

# i have already used pip to install package `five`
from five import Five
f = Five()
print(f())
print(f.loud())

