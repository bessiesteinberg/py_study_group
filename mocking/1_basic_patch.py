from unittest.mock import patch

@patch('classes.classA')
def test(mock_class_a):
	mock_class_a.method_a()
	assert mock_class_a.called
	assert mock_class_a.method_a.called