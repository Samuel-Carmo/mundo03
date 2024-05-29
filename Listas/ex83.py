expressao = input('Digite a expressão: ')
abrir = 0
fechar = 0
for i in expressao:
    if i in '(':
        abrir += 1
    elif i in ')':
        fechar += 1

if abrir == fechar:
    print('Sua expreção está valida!')
else:
    print('Sua expressão está errada!')