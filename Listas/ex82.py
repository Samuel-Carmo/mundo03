numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'A lista completa é {numeros}')
pares = []
impares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
