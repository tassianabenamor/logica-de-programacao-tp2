# Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.

n1 = float(input("Insira um número: "))
resto = n1 % 2
if (resto == 0):
    print("Número par.")
else:
    print("Número ímpar.")