from unittest.mock import patch

nato_alphabet = {
	'a': 'alpha',
	'b': 'bravo',
	'c': 'charlie'
}

with patch.dict(
	nato_alphabet,
	{'a': 'apple', 'b': 'banana', 'c': 'cantalope'},
	clear=True
	):
	print("within the `with`")
	print("nato_alphabet: {}".format(nato_alphabet))

print("out of the `with`")
print("nato_alphabet: {}".format(nato_alphabet))
