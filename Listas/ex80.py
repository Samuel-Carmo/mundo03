valores = []
for n in range(0,5):
    valor = int(input('Digite um valor: '))
    if n == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for p in range(0, len(valores)):
            if valor < valores[p]:
                print(f'adicionado na posição {p} da lista...')
                valores.insert(p, valor)
                break
print('-=' * 30)
print(f'Os valores digitados foram {valores}')