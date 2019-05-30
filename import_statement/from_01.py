from cactus import say_hello

import plantae.angiosperms.eudicots.caryophyllales.cactaceae
from plantae.angiosperms.eudicots.caryophyllales.cactaceae import say_hello

print(f"dir(say_hello): {dir(say_hello)}")
print(f"{say_hello.__module__}")

# from jellyfish import say_hello