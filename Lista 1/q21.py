# 21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. 

print('O Programa vai Informa se o Número é Primo: ')

num = int(input('\nDigite um Número Inteiro: '))

if num % num == 0 and num % 2 != 0:
    print('O número ',num,'è primo')
else:
    print('O número ',num,'não è primo')