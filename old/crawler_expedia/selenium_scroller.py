import time
import numpy as np

def page_scroller(driver, url, scroll_seconds, toFile):
    
    driver.get(url)

    random_scroll = np.random.randint(204, 1181, scroll_seconds)
    random_sleep = np.random.randint(0, 3, scroll_seconds)

    y = 0
    i = 0
    while i < scroll_seconds:
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y += random_scroll[i]
        time.sleep(random_sleep[i])
        i += 1

    html = driver.page_source

    if toFile:
        with open('C:/Users/Simo/Desktop/progetto_bda-main/crawler_expedia/html.txt', "w", encoding="utf-8") as f:
            f.write(html)

    return html