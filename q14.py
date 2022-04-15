print('14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. ')

peso = int(input('\nInforme o Peso do Peixe 0 a 100 KL '))

if peso > 50:
    excesso = peso - 50

    multa = excesso * 4

    print('\nO Peixe com Peso de',peso,'quilos, excedeu o limite em',excesso,'kl gerando uma multa de R$',multa,',00 Reais')
else:
    print('\nO Peixe com Peso de',peso,'kl, está dentro do regulamento de pesca do estado de São Paulo menor que (50 kl) ')