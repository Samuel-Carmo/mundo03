numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrao na lista!')
