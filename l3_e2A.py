# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Informe o nome de usuário: ")
senha = input(" Informe a senha: ")
while senha == nome:
    print("Senha inválida. Informe nova senha")
    senha = input(" Informe a senha: ")