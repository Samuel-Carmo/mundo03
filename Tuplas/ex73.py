times = ('Athletico-PR','Cruzeiro', 'Flamengo', 'Fortaleza', 'Vasco da Gama', 'Internacional', 'Palmeiras', 'Fluminense', 'Red Bull Bragantino', 'Criciúma', 'Juventude', 'Corinthians', 'Atlético-MG', 'Botafogo', 'Grêmio', 'São Paulo', 'Bahia', 'Atlético-GO', 'Vitória', 'Cuiabá')
print(f'Os cinco primeiros colocados são {times[:5]}')
print(F'Os quatro ultimos colocados são {times[-4: ]}')
print(f'{sorted(times)}')
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posição')
