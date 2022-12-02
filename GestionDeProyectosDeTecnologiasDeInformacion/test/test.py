import timeit
import statistics
import unittest
import requests
import asyncio

import os
import sys
dirname = os.path.dirname(__file__)
dirname = os.path.join(dirname.rsplit('/', 1)[0], 'scrapers')
sys.path.insert(1, dirname)

import puntoticket
import cinehoyts

puntoticket_setup = '''
import os
import sys
dirname = os.path.dirname(__file__)
dirname = os.path.join(dirname.rsplit('/', 1)[0], 'scrapers')
sys.path.insert(1, dirname)

import puntoticket
'''

puntoticket_code = '''
puntoticket.get_puntoticket()
'''

cinehoyts_setup = '''
import asyncio
import os
import sys
dirname = os.path.dirname(__file__)
dirname = os.path.join(dirname.rsplit('/', 1)[0], 'scrapers')
sys.path.insert(1, dirname)

import cinehoyts
'''

cinehoyts_code = '''
asyncio.get_event_loop().run_until_complete(cinehoyts.get_cinehoyts())
'''

class ScraperTester(unittest.TestCase):

  def test_json_puntoticket(self):
    puntoticket.create_json_puntoticket()
    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname.rsplit('/', 1)[0], 'scrapers')
    filename = os.path.join(dirname, 'json/puntoticket.json')
    self.assertTrue(os.path.isfile(filename))

  def test_load_puntoticket(self):
    average_time = statistics.mean(timeit.repeat(stmt=puntoticket_code, repeat=5, number=1, setup=puntoticket_setup))
    self.assertGreater(0.6, average_time)

  def test_puntoticket_status(self):
    response = requests.get('https://www.puntoticket.com/musica')
    self.assertEqual(200, response.status_code)

  def test_json_cinehoyts(self):
    cinehoyts.create_json_cinehoyts()
    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname.rsplit('/', 1)[0], 'scrapers')
    filename = os.path.join(dirname, 'json/cinehoyts.json')
    self.assertTrue(os.path.isfile(filename))

  def test_load_cinehoyts(self):
    average_time = statistics.mean(timeit.repeat(stmt=cinehoyts_code, repeat=3, number=1, setup=cinehoyts_setup))
    self.assertGreater(10, average_time)

  def test_cinehoyts_status(self):
    response = requests.get('https://cinehoyts.cl/cartelera/santiago-oriente')
    self.assertEqual(200, response.status_code)

if __name__ == '__main__':
  unittest.main()
