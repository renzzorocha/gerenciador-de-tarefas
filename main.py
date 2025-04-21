tarefas = []

def adicionarTarefa(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibirTarefas():
    for t in tarefas:
        print(f'{t[0]} - Status: {t[1]}')

def concluirTarefa(tarefa):
    global tarefas
    novaLista = []
    for t in tarefas:
        if t[0] == tarefa:
            novaLista.append((tarefa, 'concluida'))
        else:
            novaLista.append(t)
    tarefas = novaLista

adicionarTarefa('teste')
exibirTarefas()
concluirTarefa('teste')
exibirTarefas()