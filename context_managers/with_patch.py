from unittest.mock import patch

class SomeClass(object):

	def some_method(self, var):
		return var

with patch.object(
	SomeClass,
	'some_method',
	return_value='mocked_return_val'
	) as mock_method:
	
	some_instance = SomeClass()
	val = some_instance.some_method(6)
	print("[MOCKED] some_instance.some_method(6): {}".format(val))

# when the with is done, the mock is released
val = some_instance.some_method(6)
print("[NOT MOCKED] some_instance.some_method(6): {}".format(val))

# we still have access to the mock_method var
print("mock_method: {}".format(mock_method))
mock_method.assert_called_once_with(6)
