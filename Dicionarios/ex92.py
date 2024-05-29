# 35 colaboração
from datetime import date

pessoa = {}
ano_atual = date.today().year

pessoa['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = ano_atual - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35) - ano_atual

print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
