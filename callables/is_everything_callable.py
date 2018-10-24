print("Is 6 callable? {}".format( callable( 6 )))
print("Is 'beautiful is better than ugly' callable? {}".format( callable( 'beautiful is better than ugly' )))

class A():
	# class with no __call__ method
	pass

print("Is A callable? {}".format( callable( A )))

a = A()

print("Is a callable? {}".format( callable( a )))
