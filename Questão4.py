'''
Supondo que a população de um país A seja da ordem de 80000
habitantes com uma taxa anual de crescimento de 3% e que a população
de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça
um programa que calcule e escreva o número de anos necessários para
que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
'''

PaisA = 80000
PaisB = 200000
taxaA = 3.0
taxaB = 1.5
ano = 1
while (PaisA <= PaisB):
    PaisA = PaisA * (1 + taxaA)
    PaisB = PaisB * (1 + taxaB)
    ano = ano + 1
print ("População A: ", round(PaisA))
print ("População B: ", round(PaisB))
print ("Anos: ", ano)
