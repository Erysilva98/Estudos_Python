print('2- Fazer um programa que:'
'\nLeia um número inteiro qualquer'
'\nInforme se o número lido é múltiplo de 2 e 3 ao mesmo tempo')

num = int (input('Digite Um numero Inteiro: '))

if num % 2 == 0 and num % 3 == 0:
    print('O Numero ',num,'é múltiplo de 2 e de 3 ')
else:
    print('O Numero ',num,'não é múltiplo de 2 e de 3 ')