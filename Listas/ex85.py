numeros = [[], []]

for i in range(1, 8):
    temp = int(input(f'Digite o {i}° valor: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)

print('=-' *25)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
