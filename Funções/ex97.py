def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(msg.center(tamanho, ' '))
    print('~' * tamanho)


escreva('samuel')
escreva('Aprendendo Python')
escreva('No')
escreva('Curso em Video')
