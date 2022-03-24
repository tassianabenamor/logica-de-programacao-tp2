# Faça um algoritmo que receba um número inteiro, que representa um determinado mês do ano, e mostre o nome do mês correspondente. 
# Por exemplo, se for informado o número 2, algoritmo deverá exibir fevereiro. 
# O algoritmo deve validar se a entrada está correta.

mes = int(input("Insira número do mês entre 1 a 12: "))
if (mes == 1):
    print(mes,"Janeiro.")
elif (mes == 2):
    print(mes,"Fevereiro.")
elif (mes == 3):
    print(mes,"Março.")
elif (mes == 4):
    print(mes,"Abril.")
elif (mes == 5):
    print(mes,"Maio.")
elif (mes == 6):
    print(mes,"Junho.")
elif (mes == 7):
    print(mes,"Julho.")
elif (mes == 8):
    print(mes,"Agosto.")
elif (mes == 9):
    print(mes,"Setembro.")
elif (mes == 10):
    print(mes,"Outubro.")
elif (mes == 11):
    print(mes,"Novembro.")
elif (mes == 12):
    print(mes,"Dezembro.")
else:
    print("Mês inválido.")