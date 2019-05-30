# modules can have executable statements
# - run the first time it's encountered in an import
# - or if the module is run as a script
var = 1 + 3
print(var)

# Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module
