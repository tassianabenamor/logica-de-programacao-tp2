# Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. Os endereços no intervalo de 0 à 127 são classe A, de 128 à 191 são classe B, de 192 à 223 são classe C, de 224 à 239 são classe D e a partir de 240 são classe E. Faça um algoritmo que leia o primeiro octeto, no formato decimal, de um endereço IP e informe a sua classe.

ip = input("Entre com o IP inicial: ")
rede = ip.split(".")
print(rede)
ip = int(rede[0])
if ((ip >= 0) and (ip <= 127)):
    print("IP classe A")
elif ((ip >= 128) and (ip <= 191)):
    print("IP classe B")
elif ((ip >= 192) and (ip <= 223)):
    print("IP classe C")
elif ((ip >= 224) and (ip <= 239)):
    print("IP classe D")
elif (ip >= 240):
    print("IP classe E")
else:
    print("IP inválido")