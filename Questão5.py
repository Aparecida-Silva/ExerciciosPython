'''
Altere o programa anterior permitindo ao usuário informar as
populações e as taxas de crescimento iniciais. Valide a entrada e
permita repetir a operação.
'''

PaisA = int(input("Informe o número da população A: "))
taxaA = eval(input("Informe a taxa de crescimento da população A: "))
PaisB = int(input("Informe o número da população B: "))
taxaB = eval(input("Informe a taxa de crescimento da população B: "))
ano = 1    
while (PaisA <= PaisB):
    PaisA = PaisA * (1 + taxaA)
    PaisB = PaisB * (1 + taxaB)
    ano = ano + 1
print ("População A: ", round(PaisA))
print ("População B: ", round(PaisB))
print ("Anos: ", ano)
