'''
81. Crie um sistema de pontuação acadêmica - *de modo simples*
'''

def calcular_media(notas):
    return sum(notas) / len(notas)

def determinar_status(media):
    if media >= 7:
        return 'Aprovado'
    elif 5 <= media < 7:
        return 'Recuperação'
    else:
        return 'Reprovado'

def calcular_bonus(atividades):
    pontos_por_atividade = 0.5  # Pontos extras por atividade realizada
    return len(atividades) * pontos_por_atividade

def sistema_pontuacao_academica():
    alunos = {}

    while True:
        print('\nSistema de Pontuação Acadêmica com Atividades Extras')
        print('1 - Adicionar aluno e notas')
        print('2 - Registrar atividades extras')
        print('3 - Consultar aluno')
        print('4 - Exibir relatório geral')
        print('5 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do aluno: \n')
            notas = []
            for i in range(1, 5):
                nota = float(input(f'Digite a nota {i} do aluno: '))
                notas.append(nota)
            media = calcular_media(notas)
            status = determinar_status(media)
            alunos[nome] = {'notas': notas, 'media': media, 'status': status, 'atividades': []}
            print(f'Aluno {nome} adicionado com sucesso!')

        elif opcao == '2':
            nome = input('Digite o nome do aluno para registrar atividades extras: ')
            if nome in alunos:
                quantidade = int(input('Quantas atividades extras o aluno participou? '))
                for _ in range(quantidade):
                    atividade = input('Descreva a atividade (ex.: evento escolar, competição): ')
                    alunos[nome]['atividades'].append(atividade)
                bonus = calcular_bonus(alunos[nome]['atividades'])
                alunos[nome]['media'] += bonus
                alunos[nome]['status'] = determinar_status(alunos[nome]['media'])
                print(f'Atividades registradas! {nome} recebeu um bônus de {bonus:.2f} pontos.')
            else:
                print('Aluno não encontrado.')

        elif opcao == '3':
            nome = input('Digite o nome do aluno a ser consultado: \n')
            if nome in alunos:
                aluno = alunos[nome]
                print(f'\nAluno: {nome}')
                print(f'Notas: {aluno['notas']}')
                print(f'Média: {aluno['media']:.2f}')
                print(f'Status: {aluno['status']}')
                print(f'Atividades extras: {', '.join(aluno['atividades']) if aluno['atividades'] else 'Nenhuma'}')
            else:
                print('Aluno não encontrado.')

        elif opcao == '4':
            if not alunos:
                print('Nenhum aluno cadastrado.')
            else:
                print('\nRelatório Geral:\n')
                for nome, dados in alunos.items():
                    print(f'Aluno: {nome}, Média: {dados['media']:.2f}, Status: {dados['status']}, '
                        f'Atividades: {', '.join(dados['atividades']) if dados['atividades'] else 'Nenhuma'}')

        elif opcao == '5':
            print('Saindo do sistema.')
            break

        else:
            print('Opção inválida. Tente novamente.')

sistema_pontuacao_academica()
