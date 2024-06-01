jogadores = []
jogador = {}
gols = []

while True:
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partias {jogador['nome']} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    continuar = input('Quer continuar? [S/N] ').upper()[0]
    if continuar == 'N':
        break
    
print('-=' * 30)
print(f'cod {"nome":<15}{"gols":<15}total')
print('-' * 40)
for i, c in enumerate(jogadores):
    print(f'{i:>3} {c["nome"]:<15}{','.join(map(str, c["gols"])):<15}{sum(c["gols"])}')
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif dados >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {dados}!')
    elif dados < len(jogadores):
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}:')
        for i, c in enumerate(jogadores[dados]["gols"]):
            print(f'No jogo {i + 1} fez {c} gols.')
    print('-' * 40)
    
        