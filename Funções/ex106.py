from time import sleep
l = ['\033[m', #nulo
    '\033[30;42m', #verde
    '\033[30;41m', #vermelho
    '\033[30;44m', #azul
    '\033[7m' #invertido
    ]


def titulo(msg, cor=0):
    print(l[cor])
    tot = len(msg) + 4
    print('~' * tot)
    print(f'  {msg}')
    print('~' * tot)
    print(l[0],end='')
    sleep(1)


def ajuda():
    while True:
        titulo('SISTEMA DE AJUDA PYHELP', 1)
        print(l[4])
        n = input('Função ou Biblioteca > ')
        print(l[0], end='')
        if n.upper() == 'FIM':
            break
        else:
            titulo(f"Acessando o manual do comando '{n}'", 3)
            print(l[4])
            print(help(n))
            print(l[0], end='')
            sleep(2)
    titulo('ATÉ LOGO!', 2)


ajuda()