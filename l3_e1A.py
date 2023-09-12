#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário
#  informe um valor válido.


while True:
    nota = float(input("Informe o valor da nota: "))
    
    if not nota in range(1,11): 
        print ("Valor inválido. Digite um valor válido: ")
    else: 
        print ("Valor válido")
        break
    
 