# Faça um algoritmo que leia dois números e mostre o maior número.

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
if (n1 > n2):
    print("O maior número é:", n1)
elif (n2 > n1):
    print("O maior número é:", n2)
else:
    print("Os números são iguais.")