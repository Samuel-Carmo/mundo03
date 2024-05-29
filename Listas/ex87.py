matriz = [[], [], []]

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=-' * 30)

for l in matriz:
    for i in l:
        print(f'[{i:^5}] ', end='')
    print()

print('=-' * 30)
numeros_pares = sum([numero for sublista in matriz for numero in sublista if numero % 2 == 0])
print(f'A soma dos valores pares é {numeros_pares}.')
soma_terceira_coluna = sum([linha[2] for linha in matriz])
print(f'A soma dos valores da terceira coluna {soma_terceira_coluna}.')
print(f'o maior valor da segunda linha {max(matriz[1])}')