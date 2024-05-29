from random import sample
from time import sleep
print(f'''{'=' * 30}
{'JOGA NA MEGA SENA':^30}
{'=' * 30}''')
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for c in range(jogos):
    print(f'jogo {c + 1}: {sample(range(1, 101), 6)}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
