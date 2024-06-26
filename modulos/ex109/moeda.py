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


