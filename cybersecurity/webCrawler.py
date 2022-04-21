import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

wordlist = []
clean_list = []

def start(url):
#lista vacia para armazenar conteudo do site:    wordlist = []
    source_code = requests.get(url).text
#requisição dos dados da url:
    soup = BeautifulSoup(source_code, 'html.parser')

#tranforma cada div e class em texto:
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
#transforma conteudo em letra min e faz um split
        words = content.lower().split()
#
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

#função para remover simbolos indesejados:
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨&*()_+=}{[]<>,.;Q\|?'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


#criar um dicionario com cada palavra e faz contagem
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
    #aqui imprime cada palavra com seu numero de repetições:
        print("%s : %s" % (key, value))

    c = Counter(word_count)

#cria uma lista separada com o top 10 das palavras mais repetidas
    top = c.most_common(10)
    print(top)

#chama a funçao principal = start
if __name__ == '__main__':
    start('https://www.alpharithms.com/how-to-create-a-folder-in-github-repos-463022/')




