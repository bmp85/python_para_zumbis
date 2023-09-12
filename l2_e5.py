#5) Faça um Programa que leia três números e mostre o maior e o menor deles.


a, b, c = [int(p) for p  in  input("Informe 3 numeros: ").split()]

if a >= b and a >= c:
    print (f'Maior: {a}')
elif b >= c:
    print (f'Maior: {b}')
else:
    print (f'Maior: {c}')

if a <= b and a <= c:
    print (f'Menor: {a}')
elif b <= c:
    print (f'Menor: {b}')
else:
    print (f'Menor: {c}')