pessoas = []
pessoa = {}

while True:
    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.') 
        
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        continuar = input('Quer continuar? [S/N] ').upper()[0]
        if continuar  in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar in 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

idade_media = 0
for c in pessoas:
    idade_media += c['idade']
idade_media = idade_media / len(pessoas)
print(f'B) A média de idade é de {idade_media} anos.')

print('C) As mulheres cadastradas foram', end=' ')
for c in pessoas:
    if c['sexo'] in 'fF':
        print(c['nome'], end=' ')
print()

print('D) Lista das pessoas que estão acima da média:')
for c in pessoas:
    if c['idade'] > idade_media:
        print('    ', end='')
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
    
print('<< ENCERRADO >>')
