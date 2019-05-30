# If no other name is specified, and the module being imported is a top level module, the module’s name is bound in the local namespace as a reference to the imported module
import cactus
print(f"dir(): {dir()}")
cactus.say_hello()