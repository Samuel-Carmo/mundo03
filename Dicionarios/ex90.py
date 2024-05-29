d = {}
d['nome'] = input('Nome: ')
d['media'] = float(input(f'Média de {d["nome"]}: '))

if d['media'] >= 7:
    d['estado']= 'Aprovado'
if d['media'] < 7 and d['media'] >= 5:
    d['estado']= 'Recuperação'
else:
    d['estado'] = 'Replrovado'
print('-=' * 30)
print(f'  - nome é igual {d["nome"]}')
print(f'  - A média é igual a {d["media"]}')
print(f'  - situação é igual {d["estado"]}')
