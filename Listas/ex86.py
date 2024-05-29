matriz = [[], [], []]
c = 0
l = 0

for i in range(0, 9):
    matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
    c += 1
    if c == 3 :
        c = 0
        l += 1

print('=-' * 30)
for i in matriz:
    for t in i:
        print(f'[{t:^5}] ', end='')
    print()
