import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"}, limit=8)

for li in list:
    name = li.div.a.h3.text.strip()
    price = li.find("div", {"class":"proDetail"}).find("ins").text.strip().strip("TL")
    print(f"Name: {name} - Price: {price}")