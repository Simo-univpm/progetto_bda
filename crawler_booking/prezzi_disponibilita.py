import requests # libreria per generare richieste HTTP
from bs4 import BeautifulSoup as bs # libreria per scraping
import pandas as pd
from os.path import dirname, abspath
import sys
head = head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}


def OLDgetAllCampingLinks(checkin, checkout):

   # prende automaticamente gli url dei primi 25 camping da booking

  url = "https://www.booking.com/searchresults.it.html?ss=Marche%2C+Italia&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&dest_id=905&dest_type=region&search_selected=true&nflt=ht_id%3D224%3Bht_id%3D214"
  resp = requests.get(url, headers = head)
  soup = bs(resp.text, 'lxml')

  unedited_links = soup.find_all("a", {"data-testid": "title-link"}, href = True)

  urls = []
  for link in unedited_links:
    
    app_url =  link['href'].partition("?")[0]
    url = f'{app_url}?checkin={checkin};checkout={checkout};selected_currency=EUR'
    urls.append(url)

  return urls

def getAllCampingLinks(checkin, checkout):

  unedited_links = [

    "https://www.booking.com/hotel/it/nuovo-natural-village.it.html?aid=304142&label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&dest_id=437273;dest_type=hotel;dist=0;group_adults=1;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;srepoch=1656687621;srpvid=61bd698290d20026;type=total;ucfs=1&#hotelTmpl",
    "https://www.booking.com/hotel/it/centro-vacanze-la-risacca.it.html?aid=304142&label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&dest_id=1224156;dest_type=hotel;dist=0;group_adults=1;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;srepoch=1656688324;srpvid=4b726ae162ef0328;type=total;ucfs=1&#hotelTmpl",
    "https://www.booking.com/hotel/it/girasole-camping-village.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&dest_id=1356822&dest_type=hotel&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=67c46afff2ad039a&srepoch=1656688383&from_beach_sr=1&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/green-garden-village.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=distance_from_search&srpvid=23826b157bf00181&srepoch=1656688427&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/villaggio-camping-blu.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&dest_id=880763&dest_type=hotel&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=9eaf6b1ea922003b&srepoch=1656688447&from_beach_sr=1&beach_sr_walking_distance=663&beach_rating_score=8.5&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/garden-river.it.html?aid=304142&label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&dest_id=449529;dest_type=hotel;dist=0;group_adults=1;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;srepoch=1656688488;srpvid=590f6b339b770014;type=total;ucfs=1&#hotelTmpl",
    "https://www.booking.com/hotel/it/camping-village-mar-y-sierra.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&dest_id=1148489&dest_type=hotel&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=e6446b41a0730427&srepoch=1656688516&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/villaggio-cortina.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&dest_id=1361716&dest_type=hotel&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=3b9e6b81cbf70019&srepoch=1656688644&from_beach_sr=1&beach_sr_walking_distance=45&beach_rating_score=8.5&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/poggio-imperiale-marche-civitanova-marche-5.it.html?aid=304142&label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&dest_id=4957962;dest_type=hotel;dist=0;group_adults=1;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;srepoch=1656688672;srpvid=86ed6b8fcc960117;type=total;ucfs=1&#hotelTmpl",
    "https://www.booking.com/hotel/it/agriturismo-casale-civetta.it.html?aid=304142&label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&dest_id=7885843;dest_type=hotel;dist=0;group_adults=1;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;srepoch=1656688699;srpvid=d4966b9db65905e8;type=total;ucfs=1&#hotelTmpl",
    "https://www.booking.com/hotel/it/conero-azzurro.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&dest_id=1091929&dest_type=hotel&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=fed66bec27630263&srepoch=1656688858&from_beach_sr=1&beach_sr_walking_distance=104&beach_rating_score=8&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/camping-gabicce-monte.it.html?label=gen173nr-1DCAEoggI46AdIFFgEaHGIAQGYARS4ARfIAQzYAQPoAQH4AQKIAgGoAgO4Av2X_JUGwAIB0gIkNDkzZDg3YjEtYTI0YS00Y2ZkLThjNGUtNDhlOTY5MDAwNGNl2AIE4AIB&sid=f93e9038db1d430b82b11d1a4c0a4c04&aid=304142&ucfs=1&arphpl=1&dest_id=3255538&dest_type=hotel&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=732c6c0fa8440126&srepoch=1656688928&from_beach_sr=1&beach_sr_walking_distance=823&beach_rating_score=8.2&from=searchresults#hotelTmpl",
    "https://www.booking.com/hotel/it/camping-village-costa-verde.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/civettuola.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/agriturismo-la-viola-e-il-sole.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/resort-orizzonti-glamping.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/glamping-marche-nascoste-tenda-e-intero-alloggio.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/camping-pineta-urbino.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/camping-liana.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/camping-spiaggia-di-velluto.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/ai-due-camini.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/amapolas-villaggio-amp-camping.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/bungalow-verde-mare.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR",
    "https://www.booking.com/hotel/it/camping-norina.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR"

  ]

  urls = []
  for link in unedited_links:
    
    app_url =  link.partition("?")[0]
    url = f'{app_url}?checkin={checkin};checkout={checkout};selected_currency=EUR'
    urls.append(url)

  return urls

def getId(url):
  # "https://www.booking.com/hotel/it/camping-tre-archi.it.html?checkin=2022-09-17;checkout=2022-09-24;selected_currency=EUR"
  id = url.partition(".it.html")[0] # prende tutto quello prima di .it.html dall'url
  id = id.partition("it/")[2] # prende tutto quello dopo di it/ dall'url

  return id

def getAvailabilities(url):

  response = requests.get(url, headers = head)
  soup = bs(response.text, 'lxml')


  availability = [] # lista che contiene tutte le disponibilità di un camping

  available_rooms = soup.find("div", {"id": "available_rooms"})
  hprt_table_column = available_rooms.find("div", {"class": "hprt-table-column"})

  #if hprt_table_column is None: return availability # se la tabella delle disponibiltà non esiste si interrompe
  if hprt_table_column is not None:

    # si cercano tutte le righe della tabella delle disponibilità e si itera per ciascuna riga  
    tbody = hprt_table_column.find('tbody')
    all_tr = tbody.find_all('tr')

    type_found = False # per continuare correttamente l'esecuzione quando viene trovato il tipo della stanza
    id = getId(url) # chiave primaria per effettuare le operazioni di join

    for row in all_tr: # ciclando si prendono tutti i dati rilevanti della tabella delle disponbilità di booking
      table_row = []

      if not type_found:
        room_type = row.find("span", {"class": "hprt-roomtype-icon-link"})
        if room_type is not None:
          room_type = room_type.text.strip()
          type_found = True
      
      n_guests = row.find("div", {"class": "hprt-occupancy-occupancy-info"})
      if n_guests is not None:
        n_guests = n_guests.text.strip()
        n_guests = [int(s) for s in n_guests.split() if s.isdigit()][0]

      discount_price = row.find("div", {"class": "bui-f-color-destructive js-strikethrough-price prco-inline-block-maker-helper bui-price-display__original"})
      if discount_price is not None: discount_price = discount_price.text.strip()

      full_price = row.find("span", {"class": "prco-valign-middle-helper"})
      if full_price is not None: full_price = full_price.text.strip()

      table_row.append(room_type); table_row.append(n_guests); table_row.append(discount_price); table_row.append(full_price); table_row.append(url); table_row.append(id)
      availability.append(table_row)

      if "hprt-table-last-row" in row['class']: type_found = False


  return availability

def writeAvailabilitiesToExcel(dataset, checkin, checkout):

  OUTPUT_PATH = dirname(dirname(abspath(__file__)))
  OUTPUT_PATH = OUTPUT_PATH + f'/datasets/availability_dataset_{checkin}_{checkout}_booking.xlsx'
  OUTPUT_PATH = OUTPUT_PATH.replace("\\", "/")
  
  df = pd.DataFrame(dataset, columns = ["tipologia_stanza", "numero_persone", "prezzo_pieno", "prezzo_scontato", "url", "id"])
  df.to_excel(OUTPUT_PATH)

  print("dataset disponibilita' scritto su: " + OUTPUT_PATH)

def main(checkin, checkout):

  # prendo tutte le disponibilita dei vari camping
  all_campings_links = getAllCampingLinks(checkin, checkout)

  for l in all_campings_links:
    print(l)

  # le aggiungo ad una lista
  list_of_availabilities = []
  for url in all_campings_links:
    list_of_availabilities.append(getAvailabilities(url))
    print("scraping disponibilita': " + url)
  
  # riduco la dimensionalità di 1 per scriverla a db
  availabilities = []
  for list in list_of_availabilities: 
    for availability in list:
      availabilities.append(availability)

  # scrivo il dataset a db
  writeAvailabilitiesToExcel(availabilities, checkin, checkout)

# vari modi per lanciare lo scraping: 
#
# 1 - avviare lo script gui.py e impostare le date per lo scraping tramite la gui
# 2 - main("2022-09-17", "2022-09-24") --> richiamiamo il main direttamente da questo file con le date che ci interssano
# 3 - main(sys.argv[1], sys.argv[2])   --> eseguire lo script da terminale con le date passate come argomento

main("2022-09-17", "2022-09-24")
#main(sys.argv[1], sys.argv[2])

