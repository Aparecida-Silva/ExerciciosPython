'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input("Digite um nome que tenha pelo menos 3 caracteres: ")
while (len(nome) < 3):
    print("Inválido! Por favor repita o procedimento!!!")
    nome = input("Digite um nome que tenha pelo menos 3 caracteres: ")

idade = int(input("Informe a sua idade: "))
while (idade <= 0 or idade > 150):
    print("Inválido! Por favor repita o procedimento!!!")
    idade = int(input("Informe uma idade: "))

salario = eval(input("Informe o salário: "))
while (salario < 0):
    print("Inválido! Por favor repita o procedimento!!!")
    salario = eval(input("Informe o salário: "))

sexo = input("Informe o sexo; F(feminino) ou M(masculino): ")
while (sexo != "F" and sexo != "M"):
    print("Inválido! Por favor repita o procedimento!!!")
    sexo = input("Informe o sexo; F(feminino) ou M(masculino): ")

Ecivil = input("Informe o estado civil: s(solteiro), c(casado), v(viúvo), d(divorciado)")
while (Ecivil != "s" and Ecivil != "c" and Ecivil != "v" and Ecivil != "d"):
    Ecivil = input("Informe o estado civil: s(solteiro), c(casado), v(viúvo), d(divorciado)")

print("Suas informações foram válidas!")
print("Obrigado! :D")
