import requests
from bs4 import BeautifulSoup
import json
import os
from pyppeteer import launch
import asyncio

def filter_time(time):
  return time.text.strip()

async def get_cinehoyts():
  browser = await launch()

  page = await browser.newPage()
  await page.setViewport({
    'width': 640,
    'height': 48000,
    'deviceScaleFactor': 1,
  })
  URL = "https://cinehoyts.cl"
  await page.goto(URL + '/cartelera/santiago-oriente')
  page_content = await page.content()
  soup = BeautifulSoup(page_content, "html.parser")

  locations = soup.find_all("div", class_="divFecha")
  results = soup.find_all("article", class_="tituloPelicula")
  events = []

  for location in locations:
    location_name = (location.find("h2", class_="ng-binding").text.strip()).replace("?", "")
    results = location.find_all("article", class_="tituloPelicula")
    for result in results:
      trailer = result.find("a", class_="btnTrailer")["data-video"].strip()
      a = list(map(filter_time, result.find_all("time", class_="btnhorario"))) 
      times = ", ".join(a)
      events.append(
        {
          "name": result.find("a", class_="datalayer-movie").text.strip(),
          "startDate": filter_time(result.find("span", class_="ng-binding")),
          "duration": result.find("span", class_="duracion").text.strip(),
          "trailer": trailer if trailer else None,
          "location": location_name,
          "picture": result.find("figure", class_="col4").findChildren("img" , recursive=True)[0]['src'],
          "times": times
        }
      )

  return events

def create_json_cinehoyts():
  FOLDER_NAME = "json"
  dirname = os.path.dirname(__file__)
  # Crear carpeta si no existe
  if not os.path.isdir(os.path.join(dirname, FOLDER_NAME)):
    os.makedirs(os.path.join(dirname, FOLDER_NAME))

  filename = os.path.join(dirname, f'{FOLDER_NAME}/cinehoyts.json')
  events = asyncio.get_event_loop().run_until_complete(get_cinehoyts())
  with open(filename, 'w') as outfile:
    json.dump(events, outfile, ensure_ascii=False)

if __name__ == "__main__":
  create_json_cinehoyts()
