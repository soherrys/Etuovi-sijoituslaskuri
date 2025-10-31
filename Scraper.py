import requests
from bs4 import BeautifulSoup

def hae_asunnot():
    url = "https://www.etuovi.com/myytavat-asunnot/kajaani/keskusta?asuntotyyppi=yksio,kaksio"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    kohteet = []
    for card in soup.select('.list-card__content'):
        try:
            nimi = card.find('h2').text
            hinta = card.find('span', class_='price').text.replace('€','').replace(' ','').replace('\xa0','')
            kohteet.append({'nimi': nimi, 'hinta': int(hinta)})
        except:
            continue
    return kohteet
