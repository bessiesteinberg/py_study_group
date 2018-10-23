from unittest import TestCase
from basic_main import Rectangle

class TestRectangle(TestCase):
	def setUp(self):
		self.rect = Rectangle(5,10)

	# def test_area(self):
	# 	area = self.rect.area()
	# 	self.assertEqual(area, 50)

	def test_area_fails(self):
		area = self.rect.area()
		self.assertEqual(area, 5)