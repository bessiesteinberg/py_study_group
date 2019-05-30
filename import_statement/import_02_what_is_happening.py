import sys
# The `import` statement actually combines two operations:
# (1) Finding a module, loading and initializing if necessary
# (2) Defining a name or names in the local namespace for the scope where the `import` statement occurs

# print("\n-- STEP 0: The state of things before the import --")
# # - There is a list of modules that the current module knows about:
# print(sys.modules)

# print("\n-- STEP 1: Find the right module --")
# # Step 1: Find the right module
# # - Python uses `__import__` under the hood to find modules and add it to the list of modules in sys.modules
# # - NOTE: don't do this IRL, use `importlib.import_module()`
# jelly_module = __import__('jellyfish', globals(), locals(), [], 0)

# # - sys.modules now has a record of the jellyfish module and knows where to find it
# print(sys.modules)
# print(f"sys.modules['jellyfish']: {sys.modules['jellyfish']}")

# # - __import__ returns the module, but it doesn't do the mapping/assigning of names
# print(f"jelly_module: {jelly_module}")
# print(f"dir(jelly_module): {dir(jelly_module)}")
# print(f"dir(): {dir()}")

print("\n-- STEP 2: Assign the module to a name in the local namespace")
# - this is the same as
import cactus
# this: 
# cactus = __import__('cactus', globals(), locals(), [], 0)

print(f"sys.modules['cactus']: {sys.modules['cactus']}")
print(f"dir(): {dir()}")
print(f"dir(cactus): {dir(cactus)}")
