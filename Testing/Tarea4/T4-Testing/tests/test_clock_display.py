from src.clock_factory import *
from src.clock_display import *
from unittest import TestCase

class ClockDisplayTest(TestCase):
  def setUp(self):
    self.clock = ClockDisplay(limitValues=[23,60])

  def test_increment(self):
    self.clock.increment()
    self.assertEqual(self.clock.str(), "00:01")
    
  def test_clone(self):
    clone = self.clock.clone()
    self.assertEqual(clone.str(), self.clock.str())
    
  def test_invariant(self):
    self.assertTrue(self.clock.invariant())
    
  def test_clock_display(self):
    ClockDisplay(limitValues=[23,60])
    self.assertEqual(self.clock.str(), "00:00")
    
  def test_increment(self):
    clock = ClockDisplay(limitValues=[2, 2, 1])
    clock.increment()
    self.assertEqual(clock.str(), "00:01:00")
    
  # def test_default_values(self):
    # clock = ClockDisplay()
    # self.assertEqual(clock.str(), "00:00")
  
  def test_current_display(self):
    clock = ClockDisplay(limitValues=[2, 2, 1])
    clock.increment()
    clock.increment()
    self.assertEqual(clock.str(), "01:00:00")
    
  def test_current_display_mutant0(self):
    clock = ClockDisplay(limitValues=[2, 1, 1, 1, 1])
    clock.increment()
    self.assertEqual(clock.str(), "01:00:00:00:00")
    
  def test_current_display_mutant1(self):
    clock = ClockDisplay(limitValues=[2, 3, 1, 1, 17, 1])
    clock.increment()
    self.assertEqual(clock.str(), "00:00:00:00:01:00")
    
  def test_current_display_mutant2(self):
    clock = ClockDisplay(limitValues=[2, 3, 1, 1, 1, 4])
    clock.increment()
    self.assertEqual(clock.str(), "00:00:00:00:00:01")
    
  def test_prueba(self):
    clock = ClockDisplay(limitValues=[2, 3, 1])
    print(clock.invariant())
    
    
  # def test_fail_different_limits(self):
    
  #   with self.assertRaises(Exception):
  #     ClockDisplay(limitValues=[23,59])