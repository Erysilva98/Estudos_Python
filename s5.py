import random

print('5 - Fazer um programa que:'
'\nGere trios numéricos inteiros entre 0 e 200.'
'\nCaso os números sejam iguais informe o número gerados.'
'\nCaso os um dos números seja diferente dos demais gere um novo trio.'
'\nInforme quantos trio foram necessários gerar')

num1 = random.radint(0,200)
num2 = random.radint(0,200)
num3 = random.radint(0,200)

cont = 0

while num1 != num2 and num1 != num3 and num2 != num3:
    num1 = random.radint(0,200)
    num2 = random.radint(0,200)
    num3 = random.radint(0,200)

    cont += 1

print('\nOs números Iguais Formados foi',num1)
print('\nForam Necessários ',cont,'Repetições')