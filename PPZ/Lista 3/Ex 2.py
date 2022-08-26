#Ex 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

user = input('Digite seu username: ')
pw = input('Digite sua senha: ')
while user == pw:
    print('Sua senha nao pode ser igual ao username')
    pw = input('Digite sua senha: ')
else:
    print('Username e Senha gravados com sucesso')
