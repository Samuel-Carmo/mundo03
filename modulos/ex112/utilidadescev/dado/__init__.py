def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço invalido!\033[m')
        else:
            return float(entrada)
