tarefas = []

def adicionarTarefa(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)

def exibirTarefas():
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')
