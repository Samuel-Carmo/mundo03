from time import sleep

def l():
    print('-=' * 20)


def contador(a, b, c):
    l()
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(1.5)
    if c == 0:
        c = 1
    if a > b and c > 0:
        c = - c
        b = b - 1
    elif a > b and c < 0:
        b = b - 1
    if b > a and c < 0:
        c = - c
        b = b + 1
    elif b > a and c > 0:
        b = b + 1

    for n in range(a, b, c):
        sleep(0.2)
        print(n, end=' ',flush=True) 
    print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
