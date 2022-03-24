# Faça um algoritmo que leia três números e mostre o maior número.

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))
if (n1 > n2) and (n1 > n3):
    print("O maior número é:", n1)
elif (n2 > n1) and (n2 > n3):
    print("O maior número é:", n2)
elif (n3 > n1) and (n3 > n2):
    print("O maior número é:", n3)
elif (n1 == n2) and (n1 > n3):
    print("O maior número é:", n1)
elif (n1 == n2) and (n1 > n2):
    print("O maior número é:", n2)
elif (n3 == n1) and (n3 > n2):
   print("O maior número é:", n3)
else:
  print("Os números são iguais.")