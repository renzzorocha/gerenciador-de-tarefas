tarefas = []

def adicionarTarefa(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibirTarefas():
    for t in tarefas:
        print(f'{t[0]} - Status: {t[1]}')

def concluirTarefa(tarefa):
    global tarefas
    tarefas = [ ( t[0], 'concluida' ) if t[0] == tarefa else t for t in tarefas ]


adicionarTarefa('teste')
exibirTarefas()
concluirTarefa('teste')
exibirTarefas()