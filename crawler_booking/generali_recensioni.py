import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import math
from os.path import dirname, abspath
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

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

# ottiene tutti gli url dei primi 25 camping presentati nella pagina di ricerca di booking
def OLDgetAllCampingLinks():

  url = "https://www.booking.com/searchresults.it.html?ss=Marche%2C+Italia&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&dest_id=905&dest_type=region&search_selected=true&nflt=ht_id%3D224%3Bht_id%3D214"
  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  resp = requests.get(url, headers = head)
  soup = bs(resp.text, 'lxml')

  unedited_links = soup.find_all("a", {"data-testid": "title-link"}, href = True)
  return unedited_links

# prepara gli url per prendere i dati generali dei camping
def editLinksGeneral(links):

  urls = []
  for link in links:
    
    app_url =  link.partition("?")[0]
    url = f'{app_url}?checkin=;checkout=;selected_currency=EUR'
    urls.append(url)

  return urls

# prepara gli url per prendere le recensioni
def editLinksReviews(links):

  urls = []
  for link in links:

    url = link.partition("?")[0]
    url = url.replace("hotel/it", "reviews/it/hotel")
    url = url + "?r_lang=it&customer_type=total&order=completed_desc&hp_nav=0&old_page=0&order=featuredreviews&r_lang=it&rows=24&page=1"
    urls.append(url)

  return urls

def getIdGeneral(url):
  id = url.partition(".it.html")[0] # prende tutto quello prima di .it.html dall'url
  id = id.partition("it/")[2] # prende tutto quello dopo di it/ dall'url

  return id

# ottiene i dati generali dagli url editati tramite editLinksGeneral
def getGeneralData(url):

  print("scraping generali: " + url)
  camping = []

  resp = requests.get(url, headers = head)
  soup = bs(resp.text, 'lxml')

  camping_data_raw = soup.find("script", {"type": "application/ld+json"})
  data_camping_json = json.loads(camping_data_raw.string)

  camping.append(data_camping_json['name'])
  camping.append(data_camping_json['address']['streetAddress'])

  camping_description = soup.find("div", {"id": "property_description_content"})
  if camping_description is not None: camping.append(camping_description.text.strip())
  else: camping.append("No camping description")

  camping_host_description = soup.find("div", {"class": "db29ecfbe2 ca93961ea0"})
  if camping_host_description is not None: camping.append(camping_host_description.text.strip())
  else: camping.append("No camping host description")

  camping.append(getFacilities(soup))
  camping.append(url.partition("?")[0])
  camping.append(getIdGeneral(url))

  return camping

# ottine le recensioni dagli url editati tramite editLinksReviews
def getFacilities(soup):

  facilities_list = soup.find_all("div", {"class": "hotel-facilities-group"}) # prendo tutti i div con i servizi

  servizi_appoggio = []
  for facility in facilities_list:

    facility_title = facility.find("div", {"class": "bui-title__text hotel-facilities-group__title-text"})
    servizi_appoggio.append(facility_title.text.strip().upper())
    servizi_appoggio.append(": ")

    facility_attributes = facility.find_all("div", {"class": "bui-list__description"})
    for a in facility_attributes:
      servizi_appoggio.append(a.text.strip())
      servizi_appoggio.append(", ")
    
    servizi_appoggio.append("| ")
  
  servizi = ''.join(map(str, servizi_appoggio)) # dalla lista creo una stringa formattata cosi: SERVIZIO: attributo, attributo, attributo, | SERVIZIO: attr...
  return servizi

# ottine il numero delle pagine di recensioni facendo numero recensioni/24, dove 24 è il numero di recensioni per pagina
def getReviewsPage(soup):

  n_reviews_page = 0

  p_reviews = soup.find("p", {"class": "review_list_score_count"})
  if p_reviews is not None: p_reviews = p_reviews.text
  else: return n_reviews_page

  tot_reviews = [int(s) for s in p_reviews.split() if s.isdigit()][0]
  n_reviews_page = int(math.ceil(tot_reviews/24))

  return n_reviews_page

# modifica l'url per prendere tutte le pagine di recensioni per camping
# restituisce una lista con gli url modificati per accedere a tutte le recensioni di uno specifico camping
def getReviewsUrl(url, n_reviews_page):

  url_reviews = []
  page = 1

  for i in range(n_reviews_page):

    app_url =  url[:-1] + str(page) # creo tanti link quante le pagine di recensioni aggiornando l'ultimo carattere dell'url (ovvero il numero di pagina)
    url_reviews.append(app_url)

    page += 1

  return url_reviews

def getIdReviews(url):
  # https://www.booking.com/reviews/it/hotel/camping-tre-archi.it.html
  id = url.partition(".it.html")[0]
  id = id.partition("hotel/")[2]

  return id

# prende i dati delle recensioni e ritorna una lista contenente tutte le recensioni di una pagina (quindi di un url)
def getReviewsData(soup, url):

  all_reviews = []

  reviews_list = soup.find_all("div", {"class": "review_item_review"}) # tutti i div delle recensioni
  for review in reviews_list:

    review_appoggio = []

    review_vote = review.find("div", {"class": "review_item_header_score_container"})
    if review_vote is not None: review_appoggio.append(review_vote.text.strip())
    else : review_appoggio.append("no_vote")
    
    review_title = review.find("span", {"itemprop": "name"})
    if review_title is not None: review_appoggio.append(review_title.text.strip())
    else: review_appoggio.append("no_title")

    # prendo il tipo di stanza associato alla recensione (sembra sempre il terzo tag in <li class="review_info_tag">)
    all_tags = review.find_all("li", {"class": "review_info_tag"})
    if all_tags[2] is not None: review_appoggio.append(all_tags[2].text)
    else: review_appoggio.append("no room_type")

    neg_review = review.find("p", {"class": "review_neg"})
    if neg_review is not None: review_appoggio.append(neg_review.text.strip())
    else: review_appoggio.append("no negative review")
    
    pos_review = review.find("p", {"class": "review_pos"})
    if pos_review is not None: review_appoggio.append(pos_review.text.strip())
    else: review_appoggio.append("no positive review")

    review_staydate = review.find("p", {"class": "review_staydate"})
    if review_staydate is not None: review_appoggio.append(review_staydate.text.strip())
    else: review_appoggio.append("no_staydate")

    review_appoggio.append(str(url).partition("?")[0])
    review_appoggio.append(getIdReviews(url))

    all_reviews.append(review_appoggio)

  return all_reviews

# scrive il dataset dei dati generali su excel
def writeGeneralToExcel(dataset):

  OUTPUT_PATH = dirname(dirname(abspath(__file__)))
  OUTPUT_PATH = OUTPUT_PATH + f'/datasets/general_data_dataset_booking.xlsx'
  OUTPUT_PATH = OUTPUT_PATH.replace("\\", "/")

  columns = ["camping_name", "camping_address", "camping_description", "camping_host_description", "camping_facilities", "url", "id"]
  df = pd.DataFrame(dataset, columns = columns)
  df.to_excel(OUTPUT_PATH)

  print("dati generali scritti su: " + OUTPUT_PATH)

# scrive il dataset delle recensioni su excel
def writeReviewsToExcel(dataset):

  OUTPUT_PATH = dirname(dirname(abspath(__file__)))
  OUTPUT_PATH = OUTPUT_PATH + f'/datasets/review_dataset_booking.xlsx'
  OUTPUT_PATH = OUTPUT_PATH.replace("\\", "/")
  
  columns = ["reviews_vote", "reviews_title", "room_type", "reviews_negative", "reviews_positive", "review_staydate", "url", "id"]
  df = pd.DataFrame(dataset, columns = columns)
  df.to_excel(OUTPUT_PATH)

  print("recensioni scritte su: " + OUTPUT_PATH)

def main():

  links_with_general = editLinksGeneral(unedited_links) # link editati per fare scraping dei DATI dei camping
  links_with_reviews = editLinksReviews(unedited_links) # link editati per fare scraping delle RECENSIONI

  # GENERAL DATA AND SERVICES
  all_campings_general_data = []
  for url in links_with_general:

    camping = getGeneralData(url)
    all_campings_general_data.append(camping)

  writeGeneralToExcel(all_campings_general_data)


  # REVIEWS
  # estrapolo tutti gli url delle recensioni dei camping
  print("ottengo le pagine di recensioni...")
  all_review_urls = []
  for url in links_with_reviews:
  
    resp = requests.get(url, headers = head)
    soup = bs(resp.text, 'lxml')
  
    n_reviews_page = getReviewsPage(soup) # prendo il numero di pagine di recensioni
    all_review_urls.append(getReviewsUrl(url, n_reviews_page)) # genero tutti i link contenenti recensioni per tutti i camping in lista

    print(f'{n_reviews_page} pagine di recensioni per {url}')


  # estrapolo tutte le recensioni da tutti gli url
  all_reviews = []
  for list_of_url in all_review_urls:
    for url in list_of_url:
      
      response_review = requests.get(url, headers = head)
      soup_review = bs(response_review.text, 'lxml')
  
      print("scrape recensioni: " + url)
      all_reviews.append(getReviewsData(soup_review, url))
  
  all_camping_reviews = []
  for review_list in all_reviews:
    for review in review_list:
      all_camping_reviews.append(review)
  
  writeReviewsToExcel(all_camping_reviews)

main()