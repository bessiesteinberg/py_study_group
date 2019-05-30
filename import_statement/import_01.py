a = __import__('jellyfish', globals(), locals(), [], 0)
import jellyfish as b

if a is b:
	print("they are the same!")


a.helpful_class()
b.helpful_class()


# what happens if we call import jellyfish twice?
# import jellyfish
