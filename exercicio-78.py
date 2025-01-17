'''
78. Desenvolva um sistema de login
'''

usuarios = {
    'admin': 'admin@s2025',
    'ana@2024': 'a@2025',
    'Joao@567': 'j@2025',
    'Marcelo@123' : 'm@2025'
}

def sistema_login():
    
    while True:

        opcao = int(input('\n1 - Fazer login\n2 - Registrar novo usuário\n3 - Sair\n- '))

        if opcao == 1:
            username = input('Digite seu nome de usuário: ')
            senha = input('Digite sua senha: ')
            
            if username in usuarios and usuarios[username] == senha:
                print(f' Bem-vindo, {username}!')
                break
            else:
                print('Usuário ou senha incorretos. Tente novamente.')

        elif opcao == 2:
            novo_usuario = input('Escolha um nome de usuário: ')
            if novo_usuario in usuarios:
                print('Esse nome de usuário já está em uso. Tente outro.')
            else:
                nova_senha = input('Escolha uma senha: ')
                usuarios[novo_usuario] = nova_senha
                print('Usuário registrado com sucesso')

        elif opcao == 3:
            print('Saindo do sistema.')
            break

        else:
            print('Opção inválida. Tente novamente.')

sistema_login()
