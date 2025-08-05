from abc import ABC, abstractmethod
from materia.classe_materia import Materia, MateriaBase, MateriaSemPreRequisito
from estudante.classe_estudante import Estudante
from menu.menus import menu_materias, mostrar_menu 
from database.materias import materias


#este é o menu principal com o cadastro e que inclui o menu_materias()
def main():
    novo_estudante = None
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção de 1 a 6 do Menu Principal: ")
        if opcao == "1":
            novo_estudante = Estudante.cadastro_estudante(materias)
            novo_estudante.salvar_para_json('estudante.json')
        elif opcao == "2":
            if novo_estudante:
                novo_estudante.listar_materias_cadastradas(materias)
            else:
                print("\nNenhum estudante e nem matéria cadastrados ainda")
        elif opcao == "3":
            filepath = input("Digite o caminho do arquivo para carregar os dados: ")
            #se tiver um novo estudante
            if novo_estudante:
                novo_estudante.carregar_de_json(filepath)
            else:
                try:
                    #aqui há a criação de um novo estudante com as informações vazias
                    novo_estudante = Estudante("", "", [])
                    #as informações são carregadas do arquivo
                    novo_estudante.carregar_de_json(filepath)
                except FileNotFoundError:
                    print("\nO arquivo não pôde ser acessado! Verifique o diretório novamente!\n")
        elif opcao == "4":
            if novo_estudante:
                novo_estudante.listar_materias_importantes(materias) #lista matérias mais urgentes
            else:
                print("\nNenhum estudante e nem matéria cadastrados ainda")
        elif opcao == "5":
            menu_materias()
        elif opcao == "6":
            print("\nAgradecemos a preferência pelo uso do nosso programa!")
            print("Tenha um excelente semestre! :)")
            break
        else:
            print("\nOpção inválida. Digite um valor de 1 a 5.")


if __name__ == "__main__":
    main() #esta função é chamada quando a condição acima é verdadeira e o script é executado diretamente.
