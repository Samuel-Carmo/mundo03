from time import sleep

def maior(* num):
    print('-=' * 30)
    print('Analizando os valores passados...')
    sleep(2)
    for c in num:
        print(c, end=' ',flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O mairo valor informado foi {max(num)}')
    else:
        print('O maior valor informadofoi 0')
    sleep(2)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()