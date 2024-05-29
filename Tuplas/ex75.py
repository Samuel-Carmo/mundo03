numeros = (int(input('Digite um número: ')),
 int(input('Digite outro número: ')), 
 int(input('Digite mais um número: ')),
   int(input('Digite o ultimo número: ')))

print(f'Você digitou os valores {numeros}')
print(f'o valaor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'os valores pares digitados foram', end=' ')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
