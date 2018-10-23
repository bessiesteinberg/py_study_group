from unittest.mock import patch
from classes import ClassA, ClassB

@patch('classes.ClassA')
@patch('classes.ClassB')
def test(mock_class_a, mock_class_b):
	mock_class_a.method_a()
	mock_class_b.method_b()
	assert mock_class_a.called
	assert mock_class_a.method_a.called
	assert mock_class_b.called
	assert mock_class_b.method_b.called

	print(mock_class_a)
	print(mock_class_b)

	assert False