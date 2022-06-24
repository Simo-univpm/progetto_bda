import requests # libreria per generare richieste HTTP 
from bs4 import BeautifulSoup as bs # libreria per scraping
import math

url = ["https://www.tripadvisor.it/Hotel_Review-g1924689-d948494-Reviews-Natural_Village_Resort-Porto_Potenza_Picena_Potenza_Picena_Province_of_Macerata_Marche.html",
       "https://www.tripadvisor.it/Hotel_Review-g1582949-d2346767-Reviews-La_Risacca_Camping_Village_Formule_Hotel-Porto_Sant_Elpidio_Province_of_Fermo_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g1741825-d1891906-Reviews-Girasole_Eco_Family_Village-Marina_Palmense_Fermo_Province_of_Fermo_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g608900-d1146098-Reviews-Green_Garden_Camping_Village-Sirolo_Province_of_Ancona_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g194914-d2344934-Reviews-Camping_Blu_Fantasy-Senigallia_Province_of_Ancona_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g2189383-d4923901-Reviews-Centro_Vacanze_Garden_River-Altidona_Province_of_Fermo_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g2026765-d7082655-Reviews-Camping_Village_Mar_y_Sierra-San_Costanzo_Province_of_Pesaro_and_Urbino_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g2136886-d21340843-Reviews-Amapolas_Villaggio_Camping-Mombaroccio_Province_of_Pesaro_and_Urbino_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g1025201-d677045-Reviews-Villaggio_Turistico_Residence_Mare-Fermo_Province_of_Fermo_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g194914-d3309922-Reviews-Camping_Villaggio_Cortina-Senigallia_Province_of_Ancona_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g194742-d21379810-Reviews-Poggio_Imperiale_Marche-Civitanova_Marche_Province_of_Macerata_Marche.html", 
       "https://www.tripadvisor.it/Hotel_Review-g23906399-d12336250-Reviews-Casale_Civetta-Borgo_della_Consolazione_Trecastelli_Province_of_Ancona_Marche.html"]

def get_general_and_facilities(url):

  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  response = requests.get(url, headers = head)
  soup = bs(response.text, 'lxml')

  camping_general = []

  camping_name = soup.find("h1", {"class": "fkWsC b d Pn"}).text
  camping_address = soup.find("div", {"class": "ApqWZ S4 H3 f u eEkxn"}).text
  camping_about = soup.find("div", {"class": "pIRBV _T"}).text
  #camping_price = soup.find("div", {"class": "vyNCd b Wi"}) # non trova questo tag
  #camping_price = camping_price.text.strip()

  servizi_appoggio = []

  facilities = soup.find_all("div", {"class": "bUmsU f ME H3 _c"})

  for facility in facilities:
    servizi_appoggio.append(facility.text.strip())

  camping_general.append(camping_name); camping_general.append(camping_address); camping_general.append(camping_about); camping_general.append(servizi_appoggio)
  return camping_general

def get_num_reviews(url):
  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  response = requests.get(url, headers = head)
  soup = bs(response.text, 'lxml')

  num_reviews = soup.find("span", {"class": "cdKMr Mc _R b"})
  #print("> NUMERO RECENSIONI: " + num_reviews.text)

  return num_reviews

def editLinksReviews(url):

  num_reviews = int(get_num_reviews(url).text) # numero totale di recensioni per camping (5 per pagina)
  num_pag = int(math.ceil(int(num_reviews)/5)) # numero di pagine di recensione per camping
  #print("> NUMERO DI PAGINE DI RECENSIONI: " + str(num_pag))

  pag_review = 0 # variabile per incrementare di 5 in 5 l'url della pagina delle recensioni
  edited_links_reviews = [] # lista per contenere tutti gli url delle recensioni di un sito di camping
  for i in range(num_pag):
    url_appoggio = url.replace("Reviews-", f'Reviews-or{pag_review}-')
    edited_links_reviews.append(url_appoggio)
    pag_review +=5

  return edited_links_reviews

def getReviewRating(tag):
  # estrapola il voto dal tag span della recensione
  app = tag['class'][1]
  
  match app:
    case "bubble_10":
      return 1
    case "bubble_20":
      return 2
    case "bubble_30":
      return 3
    case "bubble_40":
      return 4
    case "bubble_50":
      return 5
    
    # default
    case _:
      return -1

def getReviews(url):

  # ritorna le 5 recensioni presenti nella pagina in una lista

  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  response = requests.get(url, headers = head)
  soup = bs(response.text, 'lxml')


  lista_div_recensioni = soup.find_all("div", {"class": "cWwQK MC R2 Gi z Z BB dXjiy"} and {"data-test-target": "HR_CC_CARD"})

  recensioni = []
  for div_recensioni in lista_div_recensioni:

    # utente che ha lasciato la recensione
    user = div_recensioni.find("a", {"class": "ui_header_link bPvDb"}, href = True)
    if user is not None: recensioni.append(user.text)
    else: recensioni.append("no user")

    # voto della recensione
    rating = div_recensioni.find("span", {"class": "ui_bubble_rating"})
    if rating is not None: recensioni.append(getReviewRating(rating))
    else: recensioni.append("no rating")

    # titolo della recensione
    title = div_recensioni.find("div", {"class": "fpMxB MC _S b S6 H5 _a"} and {"dir": "ltr"} and {"data-test-target": "review-title"})
    if title is not None: recensioni.append(title.text)
    else: recensioni.append("no title")

    # corpo della recensione
    review_text = div_recensioni.find("q", {"class": "XllAv H4 _a"})
    if review_text is not None: recensioni.append(review_text.text)
    else: recensioni.append("no text")

    # data di soggiorno dell'utente che ha lasciato la recensione
    stay_date = div_recensioni.find("span", {"class": "euPKI _R Me S4 H3"})
    if stay_date is not None: recensioni.append(stay_date.text)
    else: recensioni.append("no date")
  
  return recensioni
  
def main(url):

  camping_general_data_and_facilities = []
  camping_reviews_links = []

  # SCRAPING DATI GENERALI E SERVIZI | OK
  for u in url: 
    camping_general_data_and_facilities.append(get_general_and_facilities(u)) 
    print("scraping general: " + u)

  # PRENDO TUTTI I LINK CONTENENTI RECENSIONI | OK
  for u in url:
    camping_reviews_links.append(editLinksReviews(u))
    print("ottenendo i links_reviews: " + u)
  
  # SCRAPING RECENSIONI | TEST
  for reviews_links in camping_reviews_links:
    for link in reviews_links:
      print("scraping reviews: " + link)
      getReviews(link)

def testMain(url):

  # TESTING DELLE RECENSIONI:
  # il crawler sembra funzionare ma non so se prende effettivamente i dati perché non stampo nulla.
  # da testare con il camping url[11] che ha poche recensioni
  # implementare poi la scrittura su excell.

  camping_reviews_links = []

  for u in url:
    camping_reviews_links.append(editLinksReviews(u))
    print("ottenendo i links_reviews: " + u)

  for reviews_links in camping_reviews_links:
    for link in reviews_links:
      print("scraping reviews: " + link)
      getReviews(link)








#main(url)
testMain(url)