# 4) Faça um Programa que leia três números e mostre o maior deles.

a, b, c = [int(p) for p  in  input("Informe 3 numeros: ").split()]

if a == b == c:
    print("numeros iguais")
elif a > b and a > c: 
    print(f"{a:} é o maior numero ")
elif b > a and b > c: 
    print(f"{b:} é o maior numero ")
else: 
    print(f"{c:} é o maior numero ")