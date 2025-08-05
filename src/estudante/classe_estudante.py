from materia.classe_materia import Materia
import json


class Estudante:
    def __init__(self, nome, matricula, materias_em_andamento):
        self.nome = nome
        self.matricula = matricula #usar isso como parametro pra calcular qual grade trará uma formatura mais breve?
        self.materias_em_andamento = materias_em_andamento

    @classmethod
    #isso serve para realização do cadastro, opção 1 do menu principal
    def cadastro_estudante(cls, materias):
        nome_estudante = input("\nOlá. Qual o seu nome? ")
        matricula_estudante = input("\nE qual a sua matrícula? ")
        materias_em_andamento = []
        #Esse Loop serve para o usuário conseguir digitar mais de 1 matéria ao invés de ter de retornar toda vez ao menu
        while True:
            materia = input("\nDigite uma abreviação da matéria que você está cursando ou já cursou (ou digite 'sair' para finalizar): ").strip().lower()
            print("\nPara realizar a abreviação, basta digitar as iniciais e desprezar a preposição")
            print("Exemplo: Cálculo 1 vira c1; Gestão da Produção e Qualidade vira gpq;\n")
            if materia.lower() == 'sair':
                print("Saindo do cadastro...\n")
                break
            if materia in materias:
                materias[materia].status = 1 #o status é mudado para indicar que está cursando ou foi cursada
                materias_em_andamento.append(materia)
                print(f"Matéria {materia} cadastrada com sucesso!")
                print("Caso queira sair do cadastro, basta digitar sair\n")
            else:
                print(f"Matéria {materia} não encontrada.\n")

        return cls(nome_estudante, matricula_estudante, materias_em_andamento)

    def listar_materias_cadastradas(self, materias):
        print("\nMatérias cadastradas:\n")
        for materia in self.materias_em_andamento:
            if materia in materias:
                print(f"{materia}\n")
            else:
                print(f"{materia} não foi encontrada. Tente novamente.\n")

    def listar_materias_importantes(self, materias): #essa listagem não inclui matérias cadastradas pelo usuário (status == 1)
        materias_pendentes = [
            materia for materia in materias.values()
            if materia.status == 0 and isinstance(materia, Materia)
        ]

        # Ordena as matérias pendentes por número de créditos de pré-requisitos em ordem decrescente, para dar uma ênfase correta às matérias mais importantes
        top_materias = sorted(
            materias_pendentes, key=lambda materia: materia.pre_requisito, reverse=True
        )[:5]

        print("\nTop 5 matérias com maior quantidade de créditos de pré-requisitos:\n")
        for materia in top_materias: #Para cada matéria dentro das 5 encontradas acima
            print(
                f"{materia.nome} ({materia.codigo}) - Créditos de pré-requisitos: {materia.pre_requisito}\n"
            )
        print("As matérias acima deverão ser priorizadas na sua jornada. Boa sorte!\n")

    def salvar_para_json(self, filepath):
        dados_estudante = {
            'nome': self.nome,
            'matricula': self.matricula,
            'materias_cursadas_ou_cursando': self.materias_em_andamento
        }
        with open(filepath, 'w') as json_file:
            json.dump(dados_estudante, json_file, indent=4)
        print(f"Dados de {self.nome} salvos com sucesso em {filepath}\n")

    def carregar_de_json(self, filepath):
        with open(filepath, 'r') as json_file:
            dados_estudante = json.load(json_file)
        self.nome = dados_estudante['nome']
        self.matricula = dados_estudante['matricula']
        self.materias_em_andamento = dados_estudante['materias_cursadas_ou_cursando']
        print(f"\nDados de {self.nome} carregados com sucesso de {filepath}\n")