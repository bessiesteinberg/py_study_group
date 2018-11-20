# contextlib can turn a generator into a context manager! NEAT!
from contextlib import contextmanager

@contextmanager
def do_something():
	# everything before yield is considered the __enter__()
	yield some_var
	# everything after the yield is considered the __exit__()
