from rectangle import weight_of_cube, Rectangle3D
from unittest.mock import Mock

mock_rect = Mock(spec=Rectangle3D)
mock_rect.area()
mock_rect.fake_method()