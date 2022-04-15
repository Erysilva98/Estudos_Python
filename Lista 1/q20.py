# 20 - Um Programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 

nRodada = True

while nRodada == True:
    num = int (input('Informe um Número Inteiro de 1 a 15: '))

    if num > 0 and num < 16:
        result = 1
        count = 1

        while count <= num:
            result *= count
            count +=1
        print('\nO Fatorial de ',num,'é ',result)

    else:
        print('\n O Número deve ser maior que 0 e menor que 16 ')

    resp = int (input('\n Deseja calcular um novo Fatorial: SIM (1) ou NÃO (2) '))
        
    if resp == 1:
        nRodada = True
    elif resp == 2:
        nRodada = False
    elif resp != 1 and resp != 2:
        print('\nResposta Invalida:')
        resp = int (input('\n Deseja calcular um novo Fatorial: SIM (1) ou NÃO (2) '))
    




