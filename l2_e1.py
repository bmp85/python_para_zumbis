#1) Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1, lado2, lado3 = [int (p) for p in input("Informe os tres lados do triangulo: ").split()]
print(f'Lado 1: {lado1: }, Lado 2: {lado2: }, Lado 3: {lado3: }')

if lado1 > lado2 + lado3 or lado2 > lado1+lado3 or lado3 > lado1+lado2:
    print("não é um triângulo ")
elif lado1 == lado2 == lado3: 
    print("equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 ==lado3:
    print("isoceles")
else: 
    print("Escaleno")