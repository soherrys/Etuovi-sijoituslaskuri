from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import subprocess
import json
import re

def hae_asunnot():
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    chromedriver_path = subprocess.run(['which', 'chromedriver'], capture_output=True, text=True).stdout.strip()
    service = Service(chromedriver_path) if chromedriver_path else None
    
    driver = webdriver.Chrome(service=service, options=chrome_options) if service else webdriver.Chrome(options=chrome_options)
    kohteet = []
    
    try:
        url = "https://www.etuovi.com/myytavat-asunnot/kajaani/keskusta?asuntotyyppi=yksio,kaksio"
        driver.get(url)
        time.sleep(5)
        
        json_str = driver.execute_script("return JSON.stringify(window.__INITIAL_STATE__);")
        if json_str:
            data = json.loads(json_str)
            
            announcements = data.get('announcementSearch', {}).get('searchResults', {}).get('announcements', [])
            
            for announcement in announcements:
                try:
                    nimi = announcement.get('addressLine1', 'Tuntematon osoite')
                    hinta = announcement.get('searchPrice')
                    
                    if hinta and isinstance(hinta, (int, float)):
                        kohteet.append({'nimi': nimi, 'hinta': int(hinta)})
                except Exception as e:
                    continue
    except Exception as e:
        print(f"Virhe: {e}")
    finally:
        driver.quit()
    
    return kohteet

if __name__ == "__main__":
    kohteet = hae_asunnot()
    print("Löytyi", len(kohteet), "kohdetta")
    for k in kohteet:
        print(k)
