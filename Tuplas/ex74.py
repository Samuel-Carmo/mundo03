import random

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numeros_aletorios = random.sample(numeros, 5)
numeros_aletorios2 = tuple(numeros_aletorios)
print(numeros_aletorios2)
print(f'os valores sorteados foram: {numeros_aletorios2}')
print(f'O maior valor sorteado foi: {min(numeros_aletorios2)}')
print(f'O menor valor sorteado foi: {max(numeros_aletorios2)}')