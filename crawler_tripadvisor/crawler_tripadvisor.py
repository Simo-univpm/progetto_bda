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

def main(url):
  
  camping_general_data_and_facilities = []
  camping_reviews_links = []

  # DATI GENERALI E SERVIZI | OK
  for u in url: 
    camping_general_data_and_facilities.append(get_general_and_facilities(u)) 
    print("scraping general: " + u)

  # SCRAPING RECENSIONI
  for u in url:
    camping_reviews_links.append(editLinksReviews(u))
    print("ottenendo i links_reviews: " + u)


  # stampa risultati
  for elem in camping_general_data_and_facilities:
    print(elem)
    print()

  for elem in camping_reviews_links:
    print(elem)
    print()



main(url)




# TESTS ==========================================================================

#get_general_and_facilities(url[0])
#editLinksReviews(url[0])

# ================================================================================

#servizi_appoggio1 = []
#servizi_appoggio2 = []

#facilities1 = soup.find_all("div", {"class": "ccdzg S5 b Pf ME"})
#facilities2 = soup.find_all("div", {"class": "bUmsU f ME H3 _c"})

#for title in facilities1:
#  servizi_appoggio1.append(title.text.strip().upper())

#  for facility in facilities2:
#    servizi_appoggio2.append(facility.text.strip())

#print(servizi_appoggio1)
#print(servizi_appoggio2)

# ================================================================================