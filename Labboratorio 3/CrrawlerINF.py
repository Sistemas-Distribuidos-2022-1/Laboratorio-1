import requests
from bs4 import BeautifulSoup

URL = "https://www.inf.ufg.br/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())

#pesquisa o id = content e mostra o seus resultados
results = soup.find(id="content")
print(results.prettify())

categories = results.find_all("div", class_="categories")

#impimi as categorias mostradas no site
for categories in categories:
    print(categories, end="\n"*2)
