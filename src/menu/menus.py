from database.materias import materias


#Menu principal
def mostrar_menu():
    print("*** Olá. Este é o menu de cadastro das disciplinas obrigatórias de Software da FCTE ***")
    print("1 - Cadastrar estudante e matérias obrigatórias cursadas ou cursando")
    print("2 - Listar matérias já cadastradas")
    print("3 - Carregar dados de JSON")
    print("4 - Listar matérias mais urgentes")
    print("5 - Acessar menu de matérias")
    print("6 - Sair")
    

#Menu de Matérias
def listar_materias(materias):
    print("\nLista de todas as matérias:")
    for codigo, materia in materias.items():
        print(f"{codigo}: {materia.nome}")


def mostrar_descricao(materias):
    codigo = input("Digite o código da matéria: ")
    if codigo in materias:
        print(materias[codigo].descricao())
    else:
        print("Matéria não encontrada.")



def menu_materias():
    while True:
        print("\nMenu de Matérias:")
        print("1. Listar todas as matérias")
        print("2. Mostrar descrição de uma matéria")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção de 1 a 3 do Menu de Matérias: ")
        if opcao == "1":
            listar_materias(materias)
        elif opcao == "2":
            mostrar_descricao(materias)
        elif opcao == "3":
            print("Voltando ao Menu Principal...\n")
            break
        else:
            print("\nOpção inválida. Digite um valor de 1 a 3.")