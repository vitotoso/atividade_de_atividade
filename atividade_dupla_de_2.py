def adicionar_tarefa(tarefas,titulo,descricao,date_input):
    pasta={
        'Titulo': titulo,
        'Descricao': descricao,
        'Date_input': date_input,
    }
    tarefas.append(pasta)
    print("Cliente cadastrado com sucesso!")
    print("-------------------------------------------")
    print("\n")
tarefas=[]

def definir_data_entrega (tarefas,date_input,resultado):
    if date_input <= data_vencimento:
        resultado=str("aprovado")
        aprovados.append(resultado)

    else:
        
        resultado=str("vencido")
        aprovados.append(resultado)
aprovados=[]
        
def editar_tarefa(tarefas,i,titulo,descricao,date_input):
    if 0 <= i < len(tarefas):
       	tarefas[i]['Titulo'] = titulo
        tarefas[i]['Descricao'] = descricao   
        tarefas[i]['Date_input'] = date_input 
        print("\n")
        print("--------------- ATUALIZADO ---------------")
        print("Tarefa editada com sucesso!") 

def imprimir_atividade(pasta,i):
    if i in enumerate(len(pasta)):
        print("=====================================")
        print("\n")
        print("ID da tarefa",pasta[i])
        print("TITULO: ",pasta['Titulo'])
        print("DESCRIÇÂO: ",pasta['Descrição'])
        print("A TAREFA FOI ENTREGUE : ",pasta['Date_input'])
        print("A TAREFA FOI: " , aprovados[resultado])
        print("\n")
        print("=====================================")

import datetime


def deletar_atividades(tarefas,ID):
    if 0 <= ID <len(tarefas):
        print("-----------------------------------")
        del tarefas[ID]
        print("Tarefa deletada com sucesso!")
        print("-----------------------------------")
    else:
        print("Atividade não encontrada")


data_vencimento=datetime.datetime.now()
print("A data de vencimento é: ", end = "")

print (end = "") 
print (data_vencimento.day)


while True:

    print("\n")
    print("--------------- MENU ---------------")
    print("1. Adicionar tarefa.")
    print("2. Editar tarefa.")
    print("3 imprimir tarefas")
    print("4. Excluir tarefa.")
    print("5. Sair.")
    print("\n")
    op = str(input("Escolha uma opção: "))

    if op == "1":
        
        titulo = str(input("Digite o titulo da tarefa: "))
        descricao = str(input("Digite uma descrição para a tarefa: "))
        date_input = input("Digite a data de entrega: YYYY-MM-DD")
        data = datetime.datetime.strptime(date_input,"%Y-%m-%d")
        definir_data_entrega (tarefas,date_input,resultado)

        adicionar_tarefa(tarefas,titulo,descricao,date_input)

    elif op == "2":
        ID = int(input("Digite o ID da tarefa: "))
        titulo = str(input("Digite o titulo da tarefa: "))
        decricao = str(input("Digite uma descrição para a tarefa: "))
        date_input = str(input("Digite o dia para o vencimento: "))
        editar_tarefa(tarefas,ID,titulo,descricao,date_input)
        
    elif op == "3":
        imprimir_atividade(tarefas)
        
        
    elif op == "4":
        deletar_atividades(tarefas,ID)



