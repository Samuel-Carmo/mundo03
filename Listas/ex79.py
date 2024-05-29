numeros = list()
numero = 0
while True:
    numero = int(input('Digite um número: '))
    if numero in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        numeros.append(numero)
    continuar = input('Quer continuar [s/n]')
    if continuar == 'n':
        break
print('=-' * 30)
print(f'Você digitou os vaores{sorted(numeros)}')
