from unittest.mock import MagicMock


some_mock = MagicMock(side_effect=Exception('OH NO ERROR!'))
some_mock()
