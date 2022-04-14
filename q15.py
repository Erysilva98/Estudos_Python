# 15 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120 

print('Vamos Calcular o Fatorial de um Número \n')

num = int (input('Informe um Número Inteiro de 1 a 10; '))

result = 1
count = 1

while count <= num:
    result *= count
    count +=1

print('O Fatorial de ',num,'é ',result)



# resultado=1
# count=1

# while count <= numero:
#     resultado *= count
#     count += 1

# print(resultado)