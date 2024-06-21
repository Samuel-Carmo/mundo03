def ficha(nome='<desconhecido>', gols=0):
    if not gols.isnumeric():
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-' * 30)
nome = input('Nome do jogador: ')
gols = input('Números de Gols: ')
print(ficha(nome, gols))