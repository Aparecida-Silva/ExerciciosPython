'''
Faça um programa que leia 5 números e informe a soma e a média dos
números.
'''

cont = 0
a = 0
while (cont < 5):
	ent = eval(input("Digite um número: "))
	a = a + ent
	cont += 1	
print("A soma dos valores é: ",a)
print("A média dos valores é: ",a/5)
