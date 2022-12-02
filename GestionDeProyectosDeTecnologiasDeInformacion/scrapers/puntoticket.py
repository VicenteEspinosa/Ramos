import requests
from bs4 import BeautifulSoup
import json
import os


def get_puntoticket():
  URL = "https://www.puntoticket.com"
  page = requests.get(URL + '/musica')
  soup = BeautifulSoup(page.content, "html.parser")

  results = soup.find_all("div", class_="evento--box")
  events = []

  for result in results:
    description = result.find("p", class_="descripcion").text.split("/")
    dates = result.find("p", class_="fecha").text.split(" - ")
    events.append(
      {
        "name": result.find("h3").text.strip(),
        "startDate": dates[0].strip().lower(),
        "endDate": dates[1].strip().lower() if (len(dates) > 1 and dates[1].strip() != "") else None,
        "place": description[0].strip(),
        "genre": description[1].strip(),
        "url": result.parent['href'],
        "image": result.parent.find("img", class_="img--evento")['src']
      }
    )

  return events

def create_json_puntoticket():
  FOLDER_NAME = "json"
  dirname = os.path.dirname(__file__)
  # Crear carpeta si no existe
  if not os.path.isdir(os.path.join(dirname, FOLDER_NAME)):
    os.makedirs(os.path.join(dirname, FOLDER_NAME))

  filename = os.path.join(dirname, f'{FOLDER_NAME}/puntoticket.json')
  events = get_puntoticket()
  with open(filename, 'w') as outfile:
    json.dump(events, outfile, ensure_ascii=False)

if __name__ == "__main__":
  create_json_puntoticket()
