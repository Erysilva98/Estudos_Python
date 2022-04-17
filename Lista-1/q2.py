# 2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

erro = True

while erro == True:  
    nome = str (input("Informe um Nome de Usuário (sem Acentos e Minuscula) "))
    senha = str (input("Informe uma senha (não pode ser igual ao nome Usúario) "))

    if nome != senha:
        print('\n Olá!', nome, 'Bem Vindo, sua senha de acesso é:', senha)
        erro = False
    else:
        print('\n Erro, Nome de Usuário e Senha Iguais \n')
        erro = True