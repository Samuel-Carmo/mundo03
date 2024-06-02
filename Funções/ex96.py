def area(a, b):
    print(f'A área de um terreno {a}X{b} é de {a * b}m²')


print(' CONTROLE DE TERRENOS')
print('-' * 20)
largura = float(input('LARGURA (M): '))
comprimento = float(input('COMPRIMENTO (M): '))
area(largura, comprimento)
