# Faça um algoritmo que valide uma data, formada por dia, mês e ano. Por exemplo, a data 30/2 é inválida, porém a data 29/2/2012 é válida.
data = str(input("Digite sua data (Exemplo: DD/MM/AAAA): ")).split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
print("Sua data é: " + (str(dia) + "/" + str(mes) + "/" + str(ano)))
if ((dia < 0) or (mes < 0) or (ano < 0)):
    print("Data inválida. Insira valor maior que zero.")
if ((ano >= 0) and (ano % 4 == 0)):
    print("Ano bissexto.")
    if (1 <= mes <= 12):
        if ((mes == 2) and (1 <= dia <= 29)):
            print("Data válida.")
        elif (mes in (1, 3, 5, 7, 8, 10, 12) and (1 <= dia <= 31)):
            print("Mês de 31 dias.")
        elif (mes in (4, 6, 9, 11) and (1 <= dia <= 30)):
            print("Mês de 30 dias.")
        else:
            print("Data inválida. Verifique dia e mês.") 
    else:
        print("Data inválida. Insira mês entre 01 e 12.")
if ((ano >= 0) and (ano % 4 != 0)):
    print("O ano não é bissexto.")
    if (1 <= mes <= 12):
        if ((mes == 2) and (1 <= dia <= 28)):
            print("Data válida.")
        elif (mes in (1, 3, 5, 7, 8, 10, 12) and (1 <= dia <= 31)):
            print("Mês de 31 dias.")
        elif (mes in (4, 6, 9, 11) and (1 <= dia <= 30)):
            print("Mês de 30 dias.")
        else:
            print("Data inválida. Verifique dia e mês.")
    else:
        print("Data inválida. Insira mês entre 01 e 12.")
print("Fim do sistema de validação de data.")