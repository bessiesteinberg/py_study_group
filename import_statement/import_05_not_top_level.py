# If the module being imported is not a top level module, then the name of the top level package that contains the module is bound in the local namespace as a reference to the top level package. The imported module must be accessed using its full qualified name rather than directly
# import plantae.angiosperms.eudicots.caryophyllales.cactaceae
import plantae.angiosperms.eudicots.caryophyllales.cactaceae

print(f"dir(): {dir()}")
print(f"dir(plantae): {dir(plantae)}")
plantae.angiosperms.eudicots.caryophyllales.cactaceae.say_hello()
