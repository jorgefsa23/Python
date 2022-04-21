from bs4 import BeautifulSoup

import requests
#site: recebe o conteudo do site
site = requests.get("https://www.climatempo.com.br/").content
#soup: baixa do site o html
soup = BeautifulSoup(site, 'html.parser')
#prettify: transforma a string numa estrutura html

#imprime todo o html:
#print(soup.prettify())

#temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
#print(temperatura.string)

print(soup.title.string)

print(soup.a) #primeira tag áncora do site

print(soup.p.string)

print(soup.find('admin'))



