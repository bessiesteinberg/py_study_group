from contextlib import contextmanager

@contextmanager
def sandwich(bread):
	print("{}".format(bread.upper()))
	yield
	print("{}".format(bread.upper()))

with sandwich('rye'):
	print('magic deli sauce')
	print('swiss cheese')
	print('corned beef')
	print('sauerkraut')

with sandwich('everything bagel'):
	print('lox')
	print('cream cheese')