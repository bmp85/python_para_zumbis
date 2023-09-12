# 4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)