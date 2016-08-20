'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações. 
'''
usuario = input("Informe o nome: ")
senha = input("Informe a senha: ")

while (senha == usuario):
    print("Erro!")
    print("Digite uma senha que não seja igual ao nome do usuário!")
    usuario = input("Informe o nome: ")
    senha = input("Informe a senha: ")
