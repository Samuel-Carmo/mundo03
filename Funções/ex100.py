from random import randint
numeros = []

def sorteia():
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
    print('PRONTO!')


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {numeros}, tesmos {soma}')


sorteia()
somaPar()
