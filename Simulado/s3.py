print('3- Fazer um programa que exiba os 30 primeiros termos da sequência e o valor de S:'
'\nS = 2/3 + 6/4 + 3/1 + 2/6 + (-1)/3 + 6/-2...')

numerador = 2
denominador = 3

s = 0 
troca = True

print('\nS = (',numerador,'/',denominador,')',end ='')

for i in range(0,8):
    if troca:

        s = s + numerador/denominador
        temp = numerador
        numerador = denominador * 2
        denominador = temp * 2
        denominador = temp * 2
        print('+(',numerador,'/',denominador,')', end ='')
    
    else:
        
        s = s + numerador/denominador
        numerador = numerador - 3
        denominador = denominador - 3
        print('+(',numerador,'/',denominador,')', end ='')
        troca = True

print(' ')

