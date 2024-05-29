matriz = []
for l in range(0,3):
    matriz.append([])
    for c in range(0, 3):
        matriz [l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

for i in matriz:
    for p in i:
        print(f'[{p:^5}] ', end='')
    print()
