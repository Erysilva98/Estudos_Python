print('16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. ')

#  NÃO SOLUCIONADA ?!!!!!


metros = int (input('\n Informe quantos metros deseja pintar: '))

# Calcular o Metro quadrado
area = metros * metros
# Calcula o gasto de tinta em litros
litros = area / 3
# Calcla a quantidade de latas serão necessárias
latas = 18 / litros 
# Calcul a o custo total 
custo = latas * 80

print('\nCom',area,'Metros Quadrados sera necessário',round(litros),'litros de tinta')
print('\nSerão necessarias',round(latas),'Latas de tinta de 18L. Isso vai custa $:',round(custo),'Reais.')

