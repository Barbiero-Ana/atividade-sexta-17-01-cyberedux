from datetime import datetime
import re

def verificar_telefone(telefone):
    padrao = re.compile(r'^\(?\d{2}\)?\s?\d{5}-\d{4}$') #estudar essa validação
    return bool(padrao.match(telefone))


contatos = {}

while True:
    print('Digite a opção que lhe atende: ')
    decisao = int(input('\n1 - Adicionar um novo contato a lista\n2 - Verificar contatos salvos\n3 - Excluir contato\n4 - Sair do sistema\n- '))

    if decisao == 1:

        print('Digite o telefone do novo contato a ser adicionado (com DDD): ')
        telefone = input('- ')
        while not verificar_telefone(telefone):
            print("Número de telefone inválido! O formato correto é (XX) XXXXX-XXXX ou XX XXXXX-XXXX.")
            telefone = input('Digite o telefone do novo contato a ser adicionado (com DDD): ')

        nome = input("Digite o nome do contato que deseja adicionar a sua lista de contatos: ")


        print('\nFeminino\nMasculino\nPrefiro Não dizer\n')
        genero = ''
        while genero.lower() not in ['feminino', 'masculino', 'prefiro não dizer']:
            genero = input('Digite seu gênero: ')
            if genero.lower() not in ['feminino', 'masculino', 'prefiro não dizer']:
                print('Inválido! Tente novamente.')

        idade = input('Digite a idade do contato: ')
        while not idade.isdigit():
            print('Inválido! Tente novamente.')
            idade = input('Digite a idade do contato: ')
        idade = int(idade)


        print('\nDigite a data de aniversário do contato no modelo (DD/MM/AAAA)\n')
        birth = input('Digite a data de aniversário: ')
        try:
            birth_format = datetime.strptime(birth, "%d/%m/%Y")
        except ValueError:
            print("\nFormato de data inválido. Tente novamente.")
            continue

        print('\nAdicione uma descrição do contato\n')
        bio = input('\n- ')

        
        contatos[nome] = {
            'Telefone': telefone,
            'Gênero': genero,
            'Idade': idade,
            'Data de Nascimento': birth,
            'Biografia': bio,
        }

        print(f'\nContato de {nome} salvo com sucesso!\n')

    elif decisao == 2:
        
        if not contatos:
            print("Nenhum contato salvo!")
        else:
            print("\nContatos salvos:\n")
            for chave, valor in contatos.items():
                print(f"\nNome: {chave}")
                for sub_chave, sub_valor in valor.items():
                    print(f"{sub_chave}: {sub_valor}")

    elif decisao == 3:
        print('Digite o nome do contato que deseja excluir')
        nome_excluir = input('- ')
        if nome_excluir in contatos:
            del contatos[nome_excluir]
            print(f"Contato {nome_excluir} excluído com sucesso!")
        else:
            print('\nContato não encontrado na lista, tente novamente.')

    elif decisao == 4:
    
        print('Obrigado(a) por utilizar nossa agenda de contatos Cyber! Até a próxima.')
        break

    else:
        print('Opção inválida! Tente novamente.')
