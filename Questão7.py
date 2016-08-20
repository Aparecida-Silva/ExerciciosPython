'''
Faça um programa que leia 5 números e informe o maior número.
''' 

cont = 0
maiorValor = 1
while (cont < 5):
	ent = int(input("Digite um número: "))
	if (ent > maiorValor):
		maiorValor = ent
	cont += 1	
print("O maior valor é: ", maiorValor)
