# 12- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: 
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

print('O Programa Realiza a Tabuada de 1 a 10')

num = int(input('Informe o número de 1 a 10 para Obter a Tabuada: '))


for i in range(10):
    i = i + 1
    tabu = i * num
    print('\n Tabuada de',num,':',num,'X',i,'=',tabu)

 
