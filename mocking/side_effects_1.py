from unittest.mock import MagicMock

a_mock = MagicMock(side_effect=[1,2,3])
print(a_mock())
print(a_mock())
print(a_mock())
print(a_mock())