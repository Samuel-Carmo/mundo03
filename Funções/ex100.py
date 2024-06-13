from random import randint
from time import sleep
def sorteia(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(5):
        lista.append(randint(0, 10))
        sleep(0.3)
        print(lista[c], end=' ', flush=True)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
