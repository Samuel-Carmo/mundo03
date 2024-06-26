def metade(v):
    r = v / 2
    return r


def dobro(v):
    r = v * 2
    return r


def aumentar(v, p):
    r = v + v * p / 100
    return r

def diminuir(v, p):
    r = v - v * p / 100
    return r


def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')