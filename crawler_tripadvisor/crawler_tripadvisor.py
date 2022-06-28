import requests
from bs4 import BeautifulSoup as bs
import math
import pandas as pd
from os.path import dirname, abspath


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


# altri_url sono stati presi manualmente dal link di ricerca, con bs4 non ci riesco
url_ricerca = "https://www.tripadvisor.com/Search?q=camping&searchSessionId=6869D301949AE640A787F7ACAF5420761656251146515ssid&geo=187794&sid=E352E633D5854E248A7DD1D6B396DCA71656251201663&blockRedirect=true&ssrc=a&rf=5"
altri_url = [
  "https://www.tripadvisor.com/Hotel_Review-g194775-d2688714-Reviews-Don_Antonio_Camping_Village-Giulianova_Province_of_Teramo_Abruzzo.html",
  "https://www.tripadvisor.com/Hotel_Review-g528748-d4046705-Reviews-Camping_Panorama_del_Chianti-Certaldo_Tuscany.html",
  "https://www.tripadvisor.com/Hotel_Review-g194759-d4026529-Reviews-La_Mimosa_Camping-Fano_Province_of_Pesaro_and_Urbino_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g194878-d3365696-Reviews-Camping_Riccione-Riccione_Province_of_Rimini_Emilia_Romagna.html",
  "https://www.tripadvisor.com/Hotel_Review-g2002511-d2318786-Reviews-Camping_Vettore-Montegallo_Province_of_Ascoli_Piceno_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g946961-d946965-Reviews-Vigna_sul_Mar_Family_Camping_Village-Lido_di_Pomposa_Comacchio_Province_of_Ferrara_Emil.html",
  "https://www.tripadvisor.com/Hotel_Review-g796973-d2216148-Reviews-Camping_Village_Punta_Navaccia-Tuoro_sul_Trasimeno_Province_of_Perugia_Umbria.html",
  "https://www.tripadvisor.com/Hotel_Review-g194732-d1146660-Reviews-Cesenatico_Camping_Village-Cesenatico_Province_of_Forli_Cesena_Emilia_Romagna.html",
  "https://www.tripadvisor.com/Hotel_Review-g1566582-d3310023-Reviews-Camping_Monte_Prata-Castelsantangelo_sul_Nera_Province_of_Macerata_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g194742-d1993072-Reviews-Camping_Centro_Turistico_Belvedere-Civitanova_Marche_Province_of_Macerata_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g1182940-d2214794-Reviews-Camping_Village_Tahiti-Lido_delle_Nazioni_Comacchio_Province_of_Ferrara_Emilia_Romagn.html",
  "https://www.tripadvisor.com/Hotel_Review-g1582949-d2346767-Reviews-La_Risacca_Camping_Village_Formule_Hotel-Porto_Sant_Elpidio_Province_of_Fermo_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g194759-d6603161-Reviews-Camping_Stella_Maris-Fano_Province_of_Pesaro_and_Urbino_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g194838-d676423-Reviews-Conero_Azzurro-Numana_Province_of_Ancona_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g187895-d239188-Reviews-Camping_Michelangelo-Florence_Tuscany.html",
  "https://www.tripadvisor.com/Hotel_Review-g194914-d2344934-Reviews-Camping_Blu_Fantasy-Senigallia_Province_of_Ancona_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g187896-d669556-Reviews-Camping_Village_Panoramico_Fiesole-Fiesole_Tuscany.html",
  "https://www.tripadvisor.com/Hotel_Review-g730082-d1548649-Reviews-Camping_Don_Diego-Grottammare_Province_of_Ascoli_Piceno_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g187902-d1203618-Reviews-Camping_Siena_Colleverde-Siena_Tuscany.html",
  "https://www.tripadvisor.com/Hotel_Review-g2140648-d3519310-Reviews-Camping_Lpre-Ostra_Province_of_Ancona_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g676810-d255261-Reviews-Hu_Norcenni_Girasole_village-Figline_e_Incisa_Valdarno_Tuscany.html",
  "https://www.tripadvisor.com/Hotel_Review-g1741825-d1891906-Reviews-Girasole_Eco_Family_Village-Marina_Palmense_Fermo_Province_of_Fermo_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g187796-d4116318-Reviews-Camping_Paradiso-Pesaro_Province_of_Pesaro_and_Urbino_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g194858-d1815916-Reviews-Camping_Bellamare-Porto_Recanati_Province_of_Macerata_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g608900-d4817085-Reviews-Camping_Reno-Sirolo_Province_of_Ancona_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g194914-d2316135-Reviews-Camping_Summerland-Senigallia_Province_of_Ancona_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g2275905-d2250335-Reviews-Camping_Gabicce_Monte-Gabicce_Monte_Province_of_Pesaro_and_Urbino_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g187895-d6721746-Reviews-Firenze_Camping_in_Town-Florence_Tuscany.html",
  "https://www.tripadvisor.com/Hotel_Review-g608900-d1520372-Reviews-Camping_Club_Internazionale-Sirolo_Province_of_Ancona_Marche.html",
  "https://www.tripadvisor.com/Hotel_Review-g608900-d1146098-Reviews-Green_Garden_Camping_Village-Sirolo_Province_of_Ancona_Marche.html",
  ]

def getGeneralAndFacilities(url):

  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  resp = requests.get(url, headers = head)
  soup = bs(resp.text, 'lxml')

  camping_general = []

  camping_name = soup.find("h1", {"class": "fkWsC b d Pn"})
  if camping_name is not None: camping_name = camping_name.text

  camping_address = soup.find("div", {"class": "ApqWZ S4 H3 f u eEkxn"})
  if camping_address is not None: camping_address = camping_address.text

  camping_about = soup.find("div", {"class": "pIRBV _T"})
  if camping_about is not None: camping_about = camping_about.text

  camping_price = soup.find("div", {"class": "vyNCd b Wi"})
  if camping_price is not None: camping_price = camping_price.text
  else: camping_price = "non disponibile"

  lista_div_servizi = soup.find_all("div", {"class": "bUmsU f ME H3 _c"})

  servizi_app = []
  for div_servizio in lista_div_servizi:
    servizi_app.append(div_servizio.text.strip())
    servizi_app.append(", ")

  camping_facilities = ''.join(map(str, servizi_app))
  
  camping_general.append(camping_name); camping_general.append(camping_address); camping_general.append(camping_about); camping_general.append(camping_price); camping_general.append(camping_facilities)
  return camping_general

def getNumReviews(url):
  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  response = requests.get(url, headers = head)
  soup = bs(response.text, 'lxml')

  num_reviews = soup.find("span", {"class": "cdKMr Mc _R b"})
  print("> NUMERO RECENSIONI: " + num_reviews.text)

  return num_reviews

def editLinksReviews(url):

  num_reviews = int(getNumReviews(url).text) # numero totale di recensioni per camping (5 per pagina)
  num_pag = int(math.ceil(int(num_reviews)/5)) # numero di pagine di recensione per camping
  print("> NUMERO DI PAGINE DI RECENSIONI: " + str(num_pag))

  pag_review = 0 # variabile per incrementare di 5 in 5 l'url della pagina delle recensioni
  edited_links_reviews = [] # lista per contenere tutti gli url delle recensioni di un sito di camping
  for i in range(num_pag):
    url_appoggio = url.replace("Reviews-", f'Reviews-or{pag_review}-')
    edited_links_reviews.append(url_appoggio)
    pag_review +=5

  return edited_links_reviews

def getReviewRating(tag):
  # estrapola il voto dal tag span della recensione
  rating_string = tag['class'][1]

  if rating_string == "bubble_10": return 10
  if rating_string == "bubble_20": return 20
  if rating_string == "bubble_30": return 30
  if rating_string == "bubble_40": return 40
  if rating_string == "bubble_50": return 50

  if rating_string is not "bubble_10" | "bubble_20" | "bubble_30" | "bubble_40" | "bubble_50": return "no rating"

def getReviews(url):

  # ritorna le 5 recensioni presenti nella pagina in una lista

  print(">>> getting review of: " + url)

  head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
  response = requests.get(url, headers = head)
  soup = bs(response.text, 'lxml')


  lista_div_recensioni = soup.find_all("div", {"class": "cWwQK MC R2 Gi z Z BB dXjiy"} and {"data-test-target": "HR_CC_CARD"})

  recensioni = []
  for div_recensioni in lista_div_recensioni:
    app_rec = []

    # utente che ha lasciato la recensione
    user = div_recensioni.find("a", {"class": "ui_header_link bPvDb"}, href = True)
    if user is not None: app_rec.append(user.text)
    else: app_rec.append("no user")

    # voto della recensione
    rating = div_recensioni.find("span", {"class": "ui_bubble_rating"})
    if rating is not None: app_rec.append(getReviewRating(rating))
    else: app_rec.append("no rating")

    # titolo della recensione
    title = div_recensioni.find("div", {"class": "fpMxB MC _S b S6 H5 _a"} and {"dir": "ltr"} and {"data-test-target": "review-title"})
    if title is not None: app_rec.append(title.text)
    else: app_rec.append("no title")

    # corpo della recensione
    review_text = div_recensioni.find("q", {"class": "XllAv H4 _a"})
    if review_text is not None: app_rec.append(review_text.text)
    else: app_rec.append("no text")

    # data di soggiorno dell'utente che ha lasciato la recensione
    stay_date = div_recensioni.find("span", {"class": "euPKI _R Me S4 H3"})
    if stay_date is not None: app_rec.append(stay_date.text)
    else: app_rec.append("no date")

    app_rec.append(url)
    recensioni.append(app_rec)
  
  return recensioni

def writeGeneralToExcel(dataset):

  OUTPUT_PATH = dirname(dirname(abspath(__file__)))
  OUTPUT_PATH = OUTPUT_PATH + f'/datasets/general_data_dataset_tripadvisor.xlsx'
  OUTPUT_PATH = OUTPUT_PATH.replace("\\", "/")
  
  columns = ["name", "address", "about", "price", "facilities"]
  df = pd.DataFrame(dataset, columns = columns)
  df.to_excel(OUTPUT_PATH)

  print("generali scritte su file")

def writeReviewsToExcel(dataset):
  
  OUTPUT_PATH = dirname(dirname(abspath(__file__)))
  OUTPUT_PATH = OUTPUT_PATH + f'/datasets/review_dataset_tripadvisor.xlsx'
  OUTPUT_PATH = OUTPUT_PATH.replace("\\", "/")
  
  columns = ["username", "rating", "title", "review_text", "stay_date", "url"]
  df = pd.DataFrame(dataset, columns = columns)
  df.to_excel(OUTPUT_PATH)

  print("recensioni scritte su file")

def main(url):

  camping_general_data_and_facilities = [] # contiene dati generali e servizi di ogni singolo camping
  camping_reviews_links = [] # contiene tutti i link delle singole pagine di recensioni
  all_reviews = [] # contiene le singole recensioni di tutti i camping

  # SCRAPING DEI DATI GENERALI E SERVIZI ==============================================================
  for u in url: 
    camping_general_data_and_facilities.append(getGeneralAndFacilities(u)) 
    print("scraping general: " + u)

  writeGeneralToExcel(camping_general_data_and_facilities)

  #SCRAPING DELLE RECENSIONI ==========================================================================
  # estrapolo tutti i link contenenti pagine di recensioni per ogni camping e li salvo in camping_reviews_links
  camping_reviews_links = map(editLinksReviews, url)

  # ciclo ogni link contenente le pagine di recensioni
  for list_of_links in camping_reviews_links:
    for link in list_of_links:

      # per ogni pagina di recensioni estraggo le singole recensioni e le salvo in all_reviews
      page_of_reviews = getReviews(link)
      for review in page_of_reviews:
        all_reviews.append(review)
  
  writeReviewsToExcel(all_reviews) # salvo le recensioni su file

main(url)