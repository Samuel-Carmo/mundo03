import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    # print(site.read())