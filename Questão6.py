'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro. 
'''

n = 1

while (n <= 20):
    print(n)
    n = n + 1
    
print("Programa modificado: ")    
print(list(range(1 , 21 , 1)))
