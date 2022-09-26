# Progetto Big Data Analytics e Machine Learning @Univpm aa 2021/2022
## Sviluppo di Web Scrapers per Booking e Tripadvisor con progettazione di un Data Warehouse sui dati ottenuti

# Membri del gruppo
- Cucchieri Giacomo, matricola s275008
- Francalancia Simone, matricola s1102917

# Descrizione e obbiettivo del progetto
Il progetto consiste nell'effettuare lo **scraping** di alcune sorgenti dati come **Booking e Tripadvisor** tramite dei web crawler. I dati ottenuti dovranno essere sfruttati per la progettazione di un data warehouse per sostenere ed eseguire operazioni di business intelligence sui fatti interessati; nel nostro caso **disponibilità e recensioni**.
In particolar modo per ottenere i dati abbiamo sviluppato dei web crawler: dei software in grado di riconoscere e accedere automaticamente alla struttura di una pagina web in maniera tale da manipolarla per ottenerne le informazioni. Le informazioni restituite in output dai crawler vengono salvate in appositi datasets con estensione “.xlsx” nella directory “datasets” dove al suo interno sono presenti i dataset finali e tutti i passaggi intermedi che sono stati necessari per ottenerli.

## Indice
- [librerie utilizzate](#librerie-utilizzate)
- [installazione dei software necessari](#installazione-dei-software-necessari)
- [struttura directory progetto](#struttura-della-directory-del-progetto)
- [descrizione dei files](#descrizione-dei-files)
- [esecuzione del progetto](#esecuzione-del-progetto)
- [progetto demo](#progetto-demo)

## Librerie utilizzate
- Requests (https://pypi.org/project/requests/), per effettuare le chiamate HTTP verso le sorgenti
- Beautiful Soup (https://www.crummy.com/software/BeautifulSoup/), per effettuare lo scraping dei dati dai file HTML ottenuti in risposta
- Pandas (https://pandas.pydata.org/), per effettuare operazione di trasformazione dei dati e generare i datasets

## Installazione dei software necessari
Per utilizzare il materiale a disposizione in questa repo è necessario avere installato python3 (disponibile al seguente indirizzo: https://www.python.org/) e le librerie sopra elencate.
### Installazione librerie su Windows
* py -m pip install requests
* py -m pip install bs4
* py -m pip install pandas
* py -m pip install lxml
* py -m pip install openpyxl

### Installazione librerie su Linux
* pip install requests
* pip install bs4
* pip install pandas
* pip install lxml
* py -m pip install openpyxl


## Struttura della directory del progetto
```
.
|   
\---progetto_bda
    |   README.md
    |   
    +---crawler_booking
    |       generali_recensioni.py
    |       prezzi_disponibilita.py
    |           
    +---crawler_tripadvisor
    |       crawler_tripadvisor.py
    |       
    +---datasets
    |   |   availability_dataset_2022-07-30_2022-08-06_booking.xlsx
    |   |   availability_dataset_2022-08-13_2022-08-20_booking.xlsx
    |   |   availability_dataset_2022-09-24_2022-10-01_booking.xlsx
    |   |   availability_dataset_2022-11-26_2022-12-03_booking.xlsx
    |   |   general_data_dataset_booking.xlsx
    |   |   general_data_dataset_tripadvisor.xlsx
    |   |   review_dataset_booking.xlsx
    |   |   review_dataset_tripadvisor.xlsx
    |   |   
    |   +---etl
    |   |       etl.py
    |   |       ETL_disponibilita.xlsx
    |   |       ETL_recensioni.xlsx
    |   |       ETL_strutture.xlsx
    |   |       
    |   \---merged_datasets
    |           General_data_merged.xlsx
    |           Merge dei datasets.py
    |           Reviews_data_merged.xlsx
    |           
    +---documenti
    |       progettazione_datawarehouse.drawio
    |       schemi relazionali aggiornati.docx
    |       
    \---old
        |   Diagrammi.drawio
        |   gui.py
        |   
        +---backup datasets
	|	datasets.7z
        |       
        \---crawler_expedia
                selenium_scroller.py
```

## Descrizione dei files
 Il progetto è composto da 3 directory principali: crawler_booking, crawler_tripadvisor, datasets.
 
### crawler_booking
Contiene:
* generali_recensioni.py
* prezzi_disponibilita.py

ovvero gli scraper per le disponibilità, i dati generali e le recensioni dei siti di camping ottenuti da booking.

#### prezzi_disponibilita.py
Lo script "prezzi_disponibilita.py" è eseguibiletramite terminale seguendo questa sintassi:
```
py prezzi_disponibilita.py "checkin" "checkout"
```
Ad esempio il comando ```py prezzi_disponibilita.py "2022-09-17" "2022-09-24"``` effettuerà lo scraping delle disponibilità dei primi camping ritornati da booking ordinati per priorità nelle marche per il periodo specificato in argomento che va dal 17 settembre 2022 al 24 settembre 2022.

L'output dello scraper sarà automaticamente salvato nella directory "/datasets" sotto il nome "availability_datasets_checkin_checkout_booking.xlsx"


#### generali_recensioni.py
Lo script "generali_recensioni.py" è eseguibile tramite terminale seguendo questa sintassi:
```
py generali_recensioni.py
```
non vanno specificati argomenti in input in quanto si limita ad effettuare lo scraping dei dati generali e delle recensioni dei camping attuali al momento dello scraping di Booking.

L'output dello scraper sarà automaticamente salvato nella directory "/datasets" sotto il nome "general_data_dataset_booking.xlsx"

 ---

### crawler_tripadvisor
Contiene:
* crawler_tripadvisor.py

si occupa di effettuare lo scraping delle recensioni, dei dati generali e in parte anche delle disponibilità (per l'impossibilità di selezione del periodo temporale nella piattaforma).


Lo script "prezzi_disponibilita.py" è eseguibiletramite terminale seguendo questa sintassi:
```
py crawler_tripadvisor.py
```

L'output dello scraper sarà automaticamente salvato nella directory "/datasets" sotto il nome "general_data_dataset_tripadvisor.xlsx"

---
 
### datasets
Contiene:
* (directory) merged_datasets
* (directory) etl
* output vari degli scrapers sopraelencati

ovvero tutti i datasets e gli script per effettuare operazioni su di essi.

Lo script "/merged_datasets/Merge dei datasets.py" è eseguibiletramite terminale seguendo questa sintassi:
```
py "Merge dei datasets.py"
```
Questo script si occupa di unire i datasets delle strutture e delle recensioni delle due sorgenti in un unico file tramite la chiave "id" in comune tra le varie tabelle preparando l'output per lo script "/etl/etl.py".

Lo script restituirà 2 files in output nella directory "/datasets/merged_datasets/":
* General_data_merged.xlsx
* Reviews_data_merged.xlsx

Lo script "/etl/etl.py" è eseguibiletramite terminale seguendo questa sintassi:
```
py etl.py
```
Si occupa di leggere i files in "/merged_datasets" e di effettuare operazioni di cleansing dei dati preparandoli per il caricamento in un possibile Data Warehouse.

Lo script restituirà 3 files in output nella directory "/datasets/etl/":
* ETL_disponibilita.xlsx
* ETL_recensioni.xlsx
* ETL_strutture.xlsx

---

### documenti:
Contiene:
* progettazione_datawarehouse.drawio
* schemi relazionali aggiornati.docx

"progettazione_datawarehouse.drawio" contiene gli schemi concettuali e gli alberi degli attributi utili alla progettazione del datawarehouse, mentre "schemi relazionali aggiornati.docx" contiene gli schemi relazionali delle sorgenti che sono stati usati per effettuare le operazioni di reverse engineering.

Questi files sono ulteriormente discussi nella relazione di progetto.

---

### Nota:
### old
E' una directory contenete backups di datasets e di vecchio codice. Non è essenziale all'esecuzione del progetto ma è stata comunque tenuta.


Contiene la directory "/crawler_expedia/" con al suo interno un crawler sperimentale per la sorgente Expedia.
Questo crawler tutta via non è stato sviluppato ulteriormente in quanto la piattaforma ha a disposizione dei captcha insistenti e difficilmente superabili.
In particolare, il file "selenium_scroller.py" (riutilizzabile per una qualsiasi pagina web) è in grado di aprire una pagina web, scorrerla tutta facendone caricare tutti i tag html (superando lazy loading vari) e ritornare l'intero codice sorgente da dare in input a beautiful soup per effettuare lo scraping dei dati.
Inoltre contiene un prototipo di interfaccia grafica (gui.py) da usare per i crawler di booking e di tripadvisor, ma anche questa è stata abbandonata.


## Esecuzione del progetto
Il workflow per una corretta esecuzione del progetto è il seguente:

1. Ottenere i dati dalla sorgente Booking:
    - ```py prezzi_disponibilita.py "checkin" "checkout"```
    - ```py generali_recensioni.py```
2. Ottenere i dati dalla sorgene Tripadvisor:
    - ```py crawler_tripadvisor.py```
3. Unire i datasets ottenuti in output:
    - ```../datasets/merged_datasets/merge dei datasets.py```
4. Raffinare i dati ottenuti:
    - ```../datasets/etl/etl.py```
    - Nota: questo script è fortemente legato ai nomi dei files, quindi vanno rimpiazzati i nomi dei files delle disponibilità (ex: da availability_dataset_2022-09-20_2022-09-22_booking.xlsx a availability_dataset_CHECKIN_CHECKOUT_booking.xlsx) interessati all'interno del codice sorgente del file "etl.py".

Al termine dell'esecuzione avremo 3 files principali unificati, puliti e formattati in output nella directory ../datasets/etl
* ETL_disponibilita.xlsx
* ETL_recensioni.xlsx
* ETL_strutture.xlsx


## Progetto demo
E' disponibile un fork del progetto presso questo indirizzo: https://github.com/Simo-univpm/progetto_bda_demo.

L'unica differenza con l'originale è che viene effettuato lo scraping di solamente 3 camping per sorgente in maniera tale da ridurre i tempi di esecuzione per una eventuale presentazione, in quanto i tempi di esecuzione del progetto originale spazia dai 20 ai 30 minuti in base al numero di sorgenti da analizzare.
