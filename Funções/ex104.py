def leiaInt(msg):
    print('-' * 30)
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')