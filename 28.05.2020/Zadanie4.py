from bs4 import BeautifulSoup
import urllib3


url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=condensed"
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt
soup = BeautifulSoup(page.data, 'lxml')

for tr in soup.find('table').find_all('tr'):
    for td in tr.find_all('td'):
        if td.find('platform'):
            print(td.find('label').text.strip(), end=' ')
        else:
            print(td.text.strip(), end=' ')
    print()