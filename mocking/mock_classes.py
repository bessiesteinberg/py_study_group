from unittest.mock import patch
from rectangle import weight_of_cube

with patch('rectangle.Rectangle3D') as mock_rectangle3D:
	instance = mock_rectangle3D.return_value
	instance.weight.return_value = 10
	result = weight_of_cube()
	assert result == 10

	# watch out for...
	instance.fake_method.return_value = 'derp'
	assert instance.fake_method() == 'derp'