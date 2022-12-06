from src.display_number import *
from unittest import TestCase

class DisplayTest(TestCase):
  def setUp(self):
    self.displayNumber = NumberDisplay(0, 23)
    
  def test_increment(self):
    self.displayNumber.increase()
    self.assertEqual(self.displayNumber.str(), "01")
    
  def test_reset(self):
    self.displayNumber.increase()
    self.displayNumber.reset()
    self.assertEqual(self.displayNumber.str(), "00")