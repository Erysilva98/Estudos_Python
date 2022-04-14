# 8- Faça um programa que leia 5 números e informe a soma e a média dos números. 

num1 = int(input('Digite o 1° Número Inteiro: '))
num2 = int(input('Digite o 2° Número Inteiro: '))
num3 = int(input('Digite o 3° Número Inteiro: '))
num4 = int(input('Digite o 4° Número Inteiro: '))
num5 = int(input('Digite o 5° Número Inteiro: '))

soma = num1 + num2 + num3 + num4 + num5

media = soma / 5

print('A Soma dos Números é :',soma,' a Média dos números é: ',media)