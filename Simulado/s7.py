import random

print('7- azer um programa que:'
'Leia um número inteiro'
'Informe a quantidade de palpites da mega-sena referente ao número lido')

print('\nPalpites da Mega-Sena')

num = int(input('Digite Quantos Palpites deseja obter: '))

for i in range(0,num):
    n1 = random.randint(1,60)
    n2 = random.randint(1,60)

    while n1 == n2:
        n2 = random.randint(1,60)
    
    n3 = random.randint(1,60)
    while n1 == n2 or n2 == n3:
        n3 = random.randint(1,60)
    
    n4 = random.randint(1,60)
    while n1 == n4 or n2 == n4 or n3 == n4:
        n4 = random.randint(1,60)
    
    n5 = random.randint(1,60)
    while n1 == n5 or n2 == n5 or n3 == n5 or n4 == n5:
        n5 = random.randint(1,60)
    
    n6 = random.randint(1,60)
    while n1 == n6 or n2 == n6 or n3 == n6 or n4 == n6 or n5 == n6:
        n6 = random.randint(1,60)
    # Acrecenta 0 a esquerda em números menor que 10
    # Trasforma o número em String
    if n1 < 10: n1 = '0' + str(n1)
    if n2 < 10: n2 = '0' + str(n2)
    if n3 < 10: n3 = '0' + str(n3)
    if n4 < 10: n4 = '0' + str(n4)
    if n5 < 10: n5 = '0' + str(n5)
    if n6 < 10: n6 = '0' + str(n6)

    print(n1,'|',n2,'|',n3,'|',n4,'|',n5,'|',n6)