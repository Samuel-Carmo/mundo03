numero = int(input('Digite um nuúmero entre 0 e 20: '))
lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'douze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while numero < 0 or numero > 20:
  numero = int(input('Tente novamente.Digite um nuúmero entre 0 e 20: '))
print(f'Você digitou  número {lista[numero]}')