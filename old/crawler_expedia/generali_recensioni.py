from bs4 import BeautifulSoup as bs # libreria per scraping
import requests # libreria per generare richieste HTTP

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium_scroller import page_scroller
driver = webdriver.Chrome(ChromeDriverManager().install())



# legge la source della pagina da file. il file è scritto da selenium a fine scroll.
#html_file = open('C:/Users/Simo/Desktop/progetto_bda-main/crawler_expedia/html.txt', 'r', encoding = 'utf-8')
#page_source = html_file.read()
#html_file.close()



# ritorna una lista con tutti gli url dei camping italiani presenti nella prima pagina di ricerca di expedia
def get_all_campings_links(page_source, checkin, checkout):

    soup = bs(page_source, 'lxml')

    contenitore_links = soup.find("ol", {"class": "results-list no-bullet"})
    a_tag_list = contenitore_links.find_all("a", href = True)
    
    urls = []
    for a in a_tag_list:

        app_url = a['href'].partition("?")[0]
        url = f'https://www.expedia.it{app_url}?chkin={checkin}&chkout={checkout}&top_cur=EUR'
        urls.append(url)

    return urls

# ritorna i dati generali di un camping
def get_general_data(soup):

    general_data = []

    camping_name = soup.find("div", {"data-stid": "content-hotel-title"})
    if camping_name is not None: general_data.append(camping_name.text)

    camping_address = soup.find("div", {"data-stid": "content-hotel-address"})
    if camping_address is not None: general_data.append(camping_address.text)

    camping_about = soup.find("div", {"data-stid": "content-markup"})
    if camping_about is not None: general_data.append(camping_about.text)

    return general_data

# ritorna i servizi di un camping
def get_servizi(soup):

    servizi_appoggio = []

    div_tutti_servizi = soup.find("div", {"class": "uitk-card-content-section uitk-spacing uitk-card uitk-card-roundcorner-all uitk-spacing uitk-spacing-padding-block-six uitk-spacing-padding-small-inline-three uitk-spacing-padding-large-inline-six uitk-card-has-primary-theme"})
    lista_div_servizi = div_tutti_servizi.find_all("div", {"class": "uitk-layout-columns uitk-layout-columns-2 uitk-layout-columns-gap-twelve uitk-layout-columns-minwidth-half_width uitk-layout-grid-item uitk-layout-grid-item-columnspan uitk-layout-grid-item-columnspan-2"})

    for div_singolo_servizio in lista_div_servizi:
        div_singolo_servizio.find("div", {"class": "uitk-spacing uitk-spacing-margin-blockend-four"})

        for servizio in div_singolo_servizio:
            titolo = servizio.find("h3", {"class": "uitk-heading-5"})
            if titolo is not None: 
                servizi_appoggio.append(titolo.text.strip().upper())
                servizi_appoggio.append(": ")

            lista_attributi = servizio.find_all("div", {"class": "uitk-text uitk-type-300 uitk-text-default-theme"})
            for attributo in lista_attributi:
                if attributo is not None:
                    servizi_appoggio.append(attributo.text.strip())
                    servizi_appoggio.append(", ")
            servizi_appoggio.append("| ")

        #servizi_appoggio.append(url.partition("?")[0])
        servizi = ''.join(map(str, servizi_appoggio))

        return servizi


url_ricerca = "https://www.expedia.it/Hotel-Search?adults=2&d1=2022-07-02&d2=2022-07-03&destination=Italia&directFlights=false&endDate=2022-07-30&hotels-destination=Italia&latLong=41.979746669800114%2C12.448272290659107&localDateFormat=dd%2FMM%2Fyyyy&lodging=CARAVAN_PARK&partialStay=false&price=0&price=220&regionId=86&semdtl=&sort=RECOMMENDED&startDate=2022-07-23&theme=&useRewards=false&userIntent="

html_ricerca = page_scroller(driver, url_ricerca, 20, False)
camping_links = get_all_campings_links(html_ricerca, "2022-07-02", "2022-07-03")
   

for link in camping_links:
    print(link)

    resp = page_scroller(driver, link, 30, False)
    soup = bs(resp, 'lxml')

    general_data = get_general_data(soup)
    servizi = get_servizi(soup)

    camping = []
    camping.append(general_data[0]); camping.append(general_data[1]); camping.append(general_data[2])
    camping.append(servizi)

for elem in camping:
    print("> " + elem)



driver.quit()