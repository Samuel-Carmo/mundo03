def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número\033[m')
            return 0
        except:
            print('\033[31mERRO!Por favor, digite um número inteiro válido.\033[m')


def linha(tam=42):
    return '-' * tam


def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRICIPAL')
    cont = 1
    for c in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{c}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc