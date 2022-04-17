print('8- Fazer um programa que:'
'Leia três números inteiros'
'Informe o M.M.C dos números lidos\n')

maior = 5
num2 = 4
num3 = 3
mmc  = 1

for num in range(2,maior+1):
    while maior % num == 0 or num2 % num == 0 or num3 % num == 0:
        mmc = mmc * num

        if maior % num == 0: 
            maior = maior/num
        
        if num2 % num == 0:
            num2 = num2/num

        if num3 % num == 0:
            num3 = num3/num

        print('Num =',num,'Maior =',maior,'Num2 =',num2,'Num3 =',num3)

print('\nMMC =',mmc)  