lista = []
pessoa = []

maximo = minimo = 0
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        maximo = minimo = pessoa[1]
    else:
        if pessoa[1] > maximo:
            maximo = pessoa[1]
        if pessoa[1] < minimo:
            minimo = pessoa[1]
    lista.append(pessoa[:])
    continuar = input('Quer continuar? [S/N] ')
    pessoa.clear()
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maximo}Kg. Peso de ', end='')
for m in lista:
    if m[1] == maximo:
        print(f'[{m[0]}] ', end='')
print()
print(f'O menor peso foi de {minimo}Kg. Peso de ', end='')
for n in lista:
    if n[1] == minimo:
        print(f'[{n[0]}] ',end='')
print()