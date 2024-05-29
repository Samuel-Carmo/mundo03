from random import randint
jogadores = {}

jogadores['jogadpr1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')

ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
cont = 1
for k in ranking:
    print(f'   {cont}º lugar: {k[0]} com {k[1]}')
    cont += 1
print(ranking)