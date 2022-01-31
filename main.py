from bs4 import BeautifulSoup
import requests

html = requests.get("https://covid.saude.gov.br").content

# html = requests.get("https://www.climatempo.com.br/").content
    
soup = BeautifulSoup(html, 'html.parser')
selector =  "body > app-root > ion-app > ion-router-outlet > app-home > ion-content > painel-geral-component > div > card-totalizadores-component > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"

acumulado = soup.select(selector="div")

print(acumulado)
