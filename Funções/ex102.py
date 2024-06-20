def fatorial(n, show=False):
    '''-> Calcula o Fatorial de um número.
    :param n: O númeroa ser calculado.
    :param show: (opicional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.'''
    print('-' * 30)
    fatorial = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        fatorial *= c
    return fatorial

print(fatorial(5, True))
help(fatorial)
