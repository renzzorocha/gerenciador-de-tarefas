tarefas = []

def adicionarTarefa(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibirTarefas():
    if not tarefas:
        print('A lista está vazia')
        return
    for t in tarefas:
        print(f'{t[0]} - Status: {t[1]}')

def concluirTarefa(tarefa):
    global tarefas
    tarefas = [ ( t[0], 'concluida' ) if t[0] == tarefa else t for t in tarefas ]

def removerTarefa(tarefa):
    global tarefas
    tarefas = [ t for t in tarefas if t[0] != tarefa ]

def buscarTarefa(tarefa):
    global tarefas
    resultado = [ t for t in tarefas if t[0].lower() == tarefa.lower() ]
    if resultado:
        for titulo, status in resultado:
            print(f'Tarefa encontrada: {titulo} - Status: {status}')
    else:
        print('Tarefa não encontrada.')

while True:
    print('---- BOAS VINDAS AO GERENCIADOR DE LISTA DE TAREFAS ----')
    print()
    print('O que você deseja fazer?')
    print('1 - Listas tarefas')
    print('2 - Adicionar tarefa')
    print('3 - Remover tarefa')
    print('4 - Marcar tarefa como concluída')
    print('5 - Buscar tarefa')
    print('0 - Sair do Programa')
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1: 
            exibirTarefas()
        case 2: 
            tarefa = input('Digite a tarefa: ')
            adicionarTarefa(tarefa)
        case 3:
            tarefa = input('Digite a tarefa: ')
            removerTarefa(tarefa)
        case 4: 
            tarefa = input('Digite a tarefa: ')
            concluirTarefa(tarefa)
        case 5:
            tarefa = input('Digite a tarefa: ')
            buscarTarefa(tarefa)
        case 0:
            break;
        case _:
            print('Opção Inválida')


