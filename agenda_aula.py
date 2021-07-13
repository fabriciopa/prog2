#agenda: lista
#contato: dicionario
agenda = [] #lista

def incluir(agenda):
    contato = {} #dicionario
    contato["nome"] = input("Digite o Nome Completo: ")
    contato["email"] = input("Digite o Email: ")
    contato["telefone"] = input("Digite o Telefone: ")
    #adiciona um contato a agenda
    agenda.append(contato)
    
def listar(agenda):
    for index, contato in enumerate(agenda):
        print("Contato "+str(index)+":")
        print("Nome completo: "+contato["nome"])
        print("Email: "+contato["email"])
        print("Telefone: "+contato["telefone"])

def menu():
    opcao = None #null, void
    while opcao != "6":
        print("Escolha uma das opções abaixo:")
        print("1 - Incluir contato")
        print("2 - Buscar contato")
        print("3 - Editar contato")
        print("4 - Excluir contato")
        print("5 - Listar contatos")
        print("6 - Sair")

        opcao = input("Opção desejada: ")
        
        if opcao == "1":
            incluir(agenda)
        elif opcao == "2":
            buscar(agenda)
        elif opcao == "3":
            editar(agenda)
        elif opcao == "4":
            apagar(agenda)
        elif opcao == "5":
            listar(agenda)
        elif opcao == "6":
            print("Bye bye :)")
        else:
            print("Opção inválida, tente novamente!")

#Execução
menu()
