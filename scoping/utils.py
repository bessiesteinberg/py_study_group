import re

def dir_without_dunders(o):
	dir_list = dir(o) if o else dir()
	return [s for s in dir_list if not re.match(r'__.*__', s)]