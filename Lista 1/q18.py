# 18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. 

from random import randint

nMenor = 101
nMaior = 0

for i in range(10):
    num = randint(0,50)

    if num >= nMaior:
        nMaior = num
        i +=1
    elif num <= nMenor:
        nMenor = num
        i +=1


print('O Maior Número Gerado foi: ',nMaior,'\nO Menor Número foi: ',nMenor)