# 26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. 

import random 

print('Vote em favorito para Formula 1 2022 ')
print('\n     LECLERC     n° - ( 1 ) ')
print('\n     HAMILTON    n° - ( 2 ) ')
print('\n     VERSTAPEEN  n° - ( 3 ) ')

voto = int (input('\nInforme sua opção: '))

cad1 = 0
cad2 = 0
cad3 = 0

if voto == 1:
    cad1 += 1
    print('\nLECLERC foi sua escolha')
elif voto == 2:
    cad2 += 1
    print('\nHAMILTON foi sua escolha')
elif voto == 3:
    cad3 += 1
    print('\nVERSTAPEEN foi sua escolha')

cad1 += random.randint(0,20)
cad2 += random.randint(0,20)
cad3 += random.randint(0,20)

print('\nA FIA Divulgou a quantidade de votos para cada Canditado')
print('\nLECLERC com',cad1,'votos')
print('\nHAMILTON com',cad2,'votos')
print('\nVERSTAPEEN com',cad3,'votos')

if cad1 > cad2 and cad1 > cad3:
    print('\nO Vencedor é LECLERC ')
elif cad2 > cad1 and cad2 > cad3:
    print('\nO Vencedor é HAMILTON ')
elif cad3 > cad1 and cad3 > cad2:
    print('\nO Vencedor é VERSTAPEEN ')
else:
    print('Houver um empate ')