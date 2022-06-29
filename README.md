# Progetto Big Data Analytics e Machine Learning @Univpm a.a. 2021/2022
Il progetto consiste nell'effettuare lo scraping di alcune sorgenti dati come Bookin e Tripadvisor tramite dei web crawler. I dati ottenuti dovranno essere sfruttati per la progettazione di un data warehouse. In questa repo sono presenti i codice sorgenti dei vari crawler sviluppati.


La repo contiene 4 directories: crawler_booking, crawler_expedia, crawler_tripadvisor e datasets:
 
* In "crawler_booking" ci sono gli scraper per le disponibilità, i dati generali e le recensioni dei siti di camping ottenuti da booking.
Lo script "prezzi_disponibilita.py" è eseguibile tramite gui o tramite terminale seguendo questa sintassi: "py prezzi_disponibilita.py checkin checkout".
Ad esempio il comando "py prezzi_disponibilita.py 2022-09-17 2022-09-24" effettuerà lo scraping delle disponibilità dei primi 25 camping ritornati da booking ordinati per priorità nelle marche per il periodo specificato in argomento che va dal 17 settembre 2022 al 24 settembre 2022.
Lo script "generali_recensioni.py" è anch'esso eseguibile tramite gui o tramite terminale. Nel caso in cui si sceglie di eseguirlo tramite terminale con il comando "py generali_recensioni.py" non vanno specificati argomenti in input in quanto si limita ad effettuare lo scraping dei dati generali e delle recensioni dei primi 25 camping di booking.

I dati ottenuti dallo scraping verranno salvati come file excel nella directory "/datasets".

In entrambi i casi, modificando leggermente il codice si può scegliere se usare la gui o il terminale. Se viene abilitata la gui la si può avviare semplicemente con il comando "py guy.py"


* In "crawler_tripadvisor" è presente un unico file che si occupa di effettuare lo scraping delle recensioni, dei dati generali e in parte anche delle disponibilità (per l'impossibilità di selezione del periodo temporale nella piattaforma).
Allo stato d'arte lo script non dispone di gui ed è quindi eseguibile tramite terminale richiamandolo senza specificare argomenti tramite il comando "py crawler_tripadvisor.py"

Anche i dati di questo crawler verranno salvati nella directory "/datasets".

I dataset di booking e tripadvisor sono riconoscibili dai nomi dei file in quanto quelli relativi a booking terminano con "_booking" mentre quelli di tripadvisor terminano con "_tripadvisor".
  
  
* Infine in "crawler_expedia" è presente un crawler sperimentale per expedia.
Questo crawler tutta via non è stato sviluppato ulteriormente in quanto la piattaforma ha a disposizione dei captcha insistenti e difficilmente superabili. Tutta via i files sono comunque stati caricati perché potrebbero tornare utili. In particolare, il file "selenium_scroller.py" (riutilizzabile per una qualsiasi pagina web) è in grado di aprire una pagina web, scorrerla tutta facendo caricare tutti i tag html (superando lazy loading vari) e ritornare l'intero codice sorgente da dare in input a beautiful soup per effettuare lo scraping dei dati.
