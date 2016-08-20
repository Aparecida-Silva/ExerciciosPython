'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido. 
'''

nota = eval(input("Digite uma nota entre zero e dez: "))

while (nota > 10):
    print("Valor inválido!")
    nota = eval(input("Digite uma nota entre zero e dez: "))
