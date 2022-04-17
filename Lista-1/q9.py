# 9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. 

i = 1

for i in range(50):
    num = i
    if num % 2 != 0:
        print('Número Impar Gerado: ',num)
