def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'

print('-' * 20)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
