tarefas = []

def adicionarTarefa(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)

def exibirTarefas():
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    novaLista = []
    for t in tarefas:
        if(t[0] == tarefa):
            novaLista.append((tarefa, 'concluida'))
        else:
            novaLista.append(t)
        tarefas = novaLista
