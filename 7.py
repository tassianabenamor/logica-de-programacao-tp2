# Faça um algoritmo que calcule e mostre o novo valor de um salário a partir das seguintes regras: 
# salários de até R$ 1.000,00 inclusive recebem 30% de aumento, salários de até R$ 2.000,00 inclusive recebem 25%, salários de até R$ 3.000,00 inclusive recebem 20%, salários de até R$ 4.000,00 inclusive recebem 15% e salários acima de R$ 4.000,00 recebem apenas 10%.

salario = float(input("Digite seu salário: "))
if (salario <= 1000):
    novo_salario = salario * 1.30
    print("Seu novo salário é:", novo_salario)
if (salario <= 2000) and (salario >= 1000):
    novo_salario = salario * 1.25
    print("Seu novo salário é:", novo_salario)
if (salario <= 3000) and (salario >= 2000):
    novo_salario = salario * 1.20
    print("Seu novo salário é:", novo_salario)
if (salario <= 4000) and (salario >= 3000):
    novo_salario = salario * 1.15
    print("Seu novo salário é:", novo_salario)
else:
    novo_salario = salario * 1.10
    print("Seu novo salário é:", novo_salario)