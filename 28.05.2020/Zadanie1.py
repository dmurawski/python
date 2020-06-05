from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

xpath = '//*[@class="geekcentral_module leftcol"]//h2//a'

foundElements = page.xpath(xpath)
for element in foundElements :
   print(element.tag, element.keys())