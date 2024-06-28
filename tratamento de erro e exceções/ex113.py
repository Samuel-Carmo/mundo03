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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número\033[m')
            return 0
        except:
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
        


i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
