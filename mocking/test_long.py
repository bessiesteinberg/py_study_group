from unittest import TestCase
from unittest.mock import patch
from basic_main import Rectangle

class TestRectangle(TestCase):
	def setUp(self):
		self.rect = Rectangle(5,10)

	def test_without_mock(self):
		volume = self.rect.volume(6)
		self.assertEqual(volume, 300)

	# @patch('basic_main.Rectangle.volume', return_value=300)
	# def test_with_mock(self, volume):
	# 	volume = self.rect.volume(6)
	# 	self.assertEqual(volume, 300)