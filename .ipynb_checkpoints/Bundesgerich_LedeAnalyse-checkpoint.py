from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
from pathlib import Path
from datetime import date, timedelta
import time

count=1
year=2026
month=7
day=3
day=date(year,month,day)


with sync_playwright() as p:
        # Browser starten
        browser = p.chromium.launch(headless=False)

        # Neue Seite öffnen
        page = browser.new_page()


        for i in range(60):
            day_publ = day.strftime("%Y%m%d")

            url = f"https://search.bger.ch/ext/eurospider/live/de/php/aza/http/index_aza.php?date={day_publ}&lang=de&mode=news"

    
            # URL laden
            page.goto(url)

            # Warten, bis die Seite geladen ist
            page.wait_for_load_state("networkidle")
            
            
            links = []
            row_count = page.locator('xpath=//*[@id="maincontent"]/div[1]/table[2]/tbody/tr').count()

            row = 2

            for i in range(row_count // 2):
                xpath = f'xpath=//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[{row}]/td[3]/a'

                href = page.locator(xpath).get_attribute("href")
                links.append(urljoin(page.url, href))
                row += 2
            
            number=1
            for link in links:
                page.goto(link)
                page.wait_for_load_state("networkidle")
                html = page.content()
                time.sleep(0.5)
                y=str(day_publ)[0:4]
                m=str(day_publ)[4:6]
                d=str(day_publ)[6:8]
                
                
                
                Path(fr"C:\Users\misch\lede_homework_achiv\poject3-bundesgericht\original_decisions\urteil__{count}__{number}_{y}_{m}_{d}.html").write_text(html,encoding="utf-8")
                time.sleep(0.5)
                number=number+1
                count=count+1
            

                
            
        day=day-timedelta(days=1)
        time.sleep(2)

browser.close()


