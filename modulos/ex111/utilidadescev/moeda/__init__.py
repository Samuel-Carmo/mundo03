def metade(v, f=False):
    r = v / 2
    if f:    
        return moeda(r)
    else:
        return r


def dobro(v, f=False):
    r = v * 2
    if f:    
        return moeda(r)
    else:
        return r


def aumentar(v, p, f=False):
    r = v + v * p / 100
    if f:    
        return moeda(r)
    else:
        return r

def diminuir(v, p, f=False):
    r = v - v * p / 100
    if f:    
        return moeda(r)
    else:
        return r


def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')


def resumo(v, aumento=0, redução=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(v):<10}')
    print(f'{"Dobro do preço:":<20}{dobro(v, True):<10}')
    print(f'{"Metade do preço:":<20}{metade(v, True):<10}')
    print(f'{aumento}{"% de aumento:":<18}{aumentar(v, aumento, True)}')
    print(f'{redução}{"% de redução:":<18}{diminuir(v, redução, True)}')
    print('-' * 30)
    