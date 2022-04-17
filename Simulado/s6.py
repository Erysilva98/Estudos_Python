print('6- Fazer um programa que:'
'Leia N pessoas'
'Informe o nome das três pessoas mais novas')

idade1 = idade2 = idade3 = 1000
nome1 = nome2 = nome3 = ''
opcao = int(input('Digite 1 para Informar uma nova pessoa e 2 para Sair: '))

while opcao ==1:
    nome = input('Informe o nome da Pessoa: ')
    print('Informe a Idade de',nome)
    idade = int(input())

    if idade1 > idade:
        idade3 = idade3
        nome3 = nome2

        idade2 = idade1
        nome2 = nome1

        idade1 = idade
        nome1 = nome

    elif idade2 > idade:
        idade3 = idade2
        nome3 = nome2

        idade2 = idade
        nome2 = nome

    elif idade3 > idade:
        idade3 = idade
        nome3 = nome
    
    else:
        print('Idade Descartada')

    opcao = int(input('\nDigite 1 para Informar uma nova pessoa e 2 para Sair: '))

print('\n',nome1,'Primeira Pessoa mais nova com',idade1,'Anos')
print('\n',nome2,'Segunda Pessoa mais nova com',idade2,'Anos')
print('\n',nome3,'Terceira Pessoa mais nova com',idade3,'Anos')
