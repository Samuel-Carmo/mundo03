numeros = []
for p in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {p}: ')))
print('=-' * 30)
print(f'Você digitou os valores {numeros}')
print(f'O maior número digitado foi {max(numeros)} nas posições', end=' ')
for maximo in range (0, len(numeros)):
    if numeros[maximo] == max(numeros):
        print(f'{maximo}...', end=' ')
print()
print(f'O menor número digitado foi {min(numeros)} nas posições', end=' ')
for minimo in range (0, len(numeros)):
    if numeros[minimo] == min(numeros):
        print(f'{minimo}...', end=' ')
print()
