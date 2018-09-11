from unittest.mock import patch
from classes import ClassA, ClassB

@patch('classes.classA')
@patch('classes.classB')
def test(mock_class_b, mock_class_a):
	mock_class_a.method_a()
	mock_class_b.method_b()
	assert mock_class_a.called
	assert mock_class_a.method_a.called
	assert mock_class_b.called
	assert mock_class_b.method_b.called

	assert mock_class_a is ClassA
	assert mock_class_b is ClassB