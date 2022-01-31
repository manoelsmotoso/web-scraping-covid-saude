from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.climatempo.com.br/").content


soup = BeautifulSoup(html, 'html.parser')

temperatura = soup.find("span", id= "current-weather-temperature")

print(temperatura)
print("foi!")
