# a_list = [3,1,4,1,5,9,2]
# print( sorted(a_list) )

# words = ['explicatus', 'implicato', 'melior', 'est']
# print( sorted(words, key=len))

siblings_ages = {
	'alex': 31,
	'bessie': 26,
	'louis': 35,
	'tate': 21,
	'sarah': 33,
}
print( sorted(siblings_ages))
for i in siblings_ages:
	print(siblings_ages.get(i))
print( sorted(siblings_ages, key=siblings_ages.get) )
print(siblings_ages.get)
