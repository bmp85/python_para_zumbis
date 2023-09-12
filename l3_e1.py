#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário
#  informe um valor válido.

nota = float(input("Informe o valor da nota: "))

while nota < 1 or nota > 10: 
    print ("Valor inválido. Digite um valor válido: ")
    nota = float(input("Informe o valor da nota: "))
    print("Valor válido")