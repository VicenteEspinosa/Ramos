from src.clock_factory import *
from unittest import TestCase

class ClockFactoryTest(TestCase):
  def testCreate(self):
    factory = ClockFactory()
    self.assertEqual(factory.create("hh:mm").str(), "00:00")