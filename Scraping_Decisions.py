from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
from pathlib import Path
from datetime import date, timedelta
import time
import re

log_file = Path(
    r"C:\Users\misch\lede_homework_achiv\poject3-bundesgericht\scraping_log.txt"
)

def log(message):
    print(message)

    with log_file.open("a", encoding="utf-8") as file:
        file.write(message + "\n")













count=1
year=2026
month=7
day=15
day=date(year,month,day)


with sync_playwright() as p:
        # Browser starten
        browser = p.chromium.launch(headless=False)

        # Neue Seite öffnen
        page = browser.new_page()


        for i in range(300):
            day_publ = day.strftime("%Y%m%d")

            url = f"https://search.bger.ch/ext/eurospider/live/de/php/aza/http/index_aza.php?date={day_publ}&lang=de&mode=news"

    
            # URL laden
            page.goto(url)

            # Warten, bis die Seite geladen ist
            page.wait_for_load_state("networkidle")
            
            # Hier sucht Playwright alle <a>-Elemente, deren href "highlight_docid=" enthält.
            link_a_elements = page.locator('a[href*="highlight_docid="]')
            number_of_decisions = link_a_elements.count()
            
            
            if number_of_decisions<1:
                log(f"am {day_publ} wurden keine Urteile gefunden")
                


            links = []
            for link_index in range(number_of_decisions):
                decision_url = link_a_elements.nth(link_index).get_attribute("href")
                if decision_url:
                    links.append(decision_url)
                    
                else:
                    log(f"{link_index} Fail! decisision not found")
            
            number=1
            for link in links:
                match = re.search(r"\d+[A-Z]_[0-9]+-\d{4}", link)
                aktenzeichen = match.group()
                
                
                page.goto(link)
                page.wait_for_load_state("networkidle")
                html = page.content()
                time.sleep(0.5)
                y=str(day_publ)[0:4]
                m=str(day_publ)[4:6]
                d=str(day_publ)[6:8]
                
                
                
                Path(fr"C:\Users\misch\lede_homework_achiv\project3-bundesgericht\original_decisions\urteil__{count}__{number}_{y}_{m}_{d}__{aktenzeichen}.html").write_text(html,encoding="utf-8")
                time.sleep(0.5)
                number=number+1
                count=count+1 
                    
            
            day=day-timedelta(days=1)
            time.sleep(2)

browser.close()


