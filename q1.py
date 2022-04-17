print('1- Faça um Programa que peça dois números e imprima o maior deles.')

num1 = int (input('Informe o 1° Número: '))
num2 = int (input('Informe o 2° Número: '))

if num1 > num2:
    print('O Maior Número digitado é:',num1)
elif num2 > num1:
    print('O Maior Número digitado é:',num2)
else:
    print('Os Número digitado são iguais:',num1,'e',num2)