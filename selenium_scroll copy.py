from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests # libreria per generare richieste HTTP 
from bs4 import BeautifulSoup as bs # libreria per scraping

# stack overflow: https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.expedia.it/Rome-Hotel-Happy-Village-Camping.h2045230.Informazioni-Hotel?chkin=2022-07-23&chkout=2022-07-30&x_pwa=1&rfrr=HSR&pwa_ts=1654029172931&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5pdC9Ib3RlbC1TZWFyY2g%3D&useRewards=false&rm1=a2&regionId=86&destination=Italia&destType=MARKET&neighborhoodId=553248635976382290&hotelName=camping&sort=RECOMMENDED&top_dp=343&top_cur=EUR&semdtl=&userIntent=&selectedRoomType=BUN.EY&selectedRatePlan=20220723%7C20220730%7CW%7C207%7C200828%7CBUN.EY%7CNRF-BAR%7CRO%7C%7C1%7E2%7E0%7C%7CN%7C%7CB2C"
driver.get(url)

# code: https://stackoverflow.com/questions/51798987/scroll-down-to-end-page-using-selenium-python-chromedriver
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4)")
#time.sleep(20)



# ===========================================================================
# prove selenium
y = 1000
for timer in range(0,25):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 500  
    time.sleep(1)
    #driver.implicitly_wait(0.5)

html = driver.page_source

#with open('asd.txt', "w", encoding="utf-8") as f:
#    f.write(html)

soup = bs(html, 'lxml')
#print(soup)

#div data-stid="content-hotel-title"
camping_name = soup.find("div", {"data-stid": "content-hotel-title"})
if camping_name is not None: camping_name = camping_name.text

camping_address = soup.find("div", {"data-stid": "content-hotel-address"})
if camping_address is not None: camping_address = camping_address.text

camping_about = soup.find("div", {"data-stid": "content-markup"})
if camping_about is not None: camping_about = camping_about.text

tutti_i_prezzi = soup.find_all("div", {"class": "uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme"})
if tutti_i_prezzi is not None:
    prezzi = []
    for prezzo in tutti_i_prezzi:
        prezzi.append(prezzo.text.strip())
        print(prezzo)


div_servizi = soup.find("div", {"class": "uitk-card-content-section uitk-spacing uitk-card uitk-card-roundcorner-all uitk-spacing uitk-spacing-padding-block-six uitk-spacing-padding-small-inline-three uitk-spacing-padding-large-inline-six uitk-card-has-primary-theme"})
lista_servizi = div_servizi.find_all("div", {"class": "uitk-spacing uitk-spacing-padding-blockend-six"})

print(div_servizi)
for aaaa in lista_servizi:
    print(aaaa)

servizi = []
for servizio in lista_servizi:

    titolo = servizio.find("h3", {"class": "uitk-heading-5"})
    
    lista_attributi = servizio.find_all("div", {"class": "uitk-text uitk-type-300 uitk-text-default-theme"})
    attributi_servizi = []
    for attributo in lista_attributi:
        if attributo is not None:
            attributo = attributo.text.strip()
            attributi_servizi.append(attributo)

    servizi.append(titolo)
    servizi.append(attributi_servizi)


for s in servizi:
    print(s)



print("> NOME: " +  str(camping_name))
print("> INDIRIZZO: " + str(camping_address))
print("> DESCRIZIONE: " + str(camping_about))
#print("> PREZZO: " + str(prezzo))

driver.quit()