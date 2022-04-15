print('13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:')

# Para homens: (72.7*h) - 58')
# Para mulheres: (62.1*h) - 44.7')

sexo = int (input('\nInforme seu Sexo : (1) Masculino ou (2) Feminino '))
nome = str (input('\nDigite seu Nome: '))
h    = float (input('\nInforme sua Altura ex:(1.50) : '))

if sexo == 1:
    peso = (72.7 * h) - 58
    print('\nO Peso Ideal para',nome,'é ',peso)

elif sexo == 2:
    peso = (62.1 * h) - 44.7
    print('\nO Peso Ideal para',nome,'é ',peso)
else:
    print('\nOpção de sexo Invalida')