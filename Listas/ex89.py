lista = []
cont = 0
aluno = 0
temp = ()
while True:
    lista.append([])
    lista[cont].append(input('Nome: '))
    lista[cont].append(float(input('Nota 1: ')))
    lista[cont].append(float(input('Nota 2: ')))
    continuar = input('Quer continuar? [S/N] ')
    cont += 1
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('=' * 26)
for i, c in enumerate(lista):
    media =( c[1] + c[2]) / 2
    print(f'{i:<4}{c[0]:<10}{media:>8.1f}')
while True:
    print('=' * 35)
    if aluno == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno >= cont:
        print('Aluno não existe')
    else:
        temp = lista[aluno]
        print(f'Notas de {temp[0]} são {temp[1:]}')

