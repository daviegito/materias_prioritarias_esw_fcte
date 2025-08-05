from materia.classe_materia import Materia, MateriaBase, MateriaSemPreRequisito
import json

materias = {
    #No momento, o usuário terá de digitar "c1", "apc" e afins sem as aspas.
    # 1 semestre
    "c1": Materia("Cálculo 1", "MAT0025", 6, 22, 0),
    "apc": Materia("Algoritmos e Programação de Computadores", "CIC0004", 6, 74, 0),
    "diac": MateriaSemPreRequisito("Desenho Industrial Assistido por Computador", "FGA0168", 6, 0),
    "ea": MateriaSemPreRequisito("Engenharia e Ambiente", "FGA0161", 4, 0),
    "ie": MateriaSemPreRequisito("Introdução à Engenharia", "FGA0163", 2, 0),
    # 2 semestre
    "c2": Materia("Cálculo 2", "MAT0026", 6, 4, 0),
    "f1": MateriaSemPreRequisito("Física 1", "IFD0171", 4, 0),
    "f1e": MateriaSemPreRequisito("Física 1 Experimental", "IFD0173", 2, 0),
    "ial": Materia("Introdução à Álgebra Linear", "MAT0031", 4, 26, 0),
    "peae": MateriaSemPreRequisito("Probabilidade e Estatística Aplicada à Engenharia", "FGA0157", 4, 0),
    # 3 semestre
    "mne": MateriaSemPreRequisito("Métodos Numéricos para Engenharia", "FGA0160", 4, 0),
    "ee": Materia("Engenharia Econômica", "FGA0133", 4, 8, 0),
    "hc": MateriaSemPreRequisito("Humanidades e Cidadania", "FGA0164", 2, 0),
    "ted1": Materia("Teoria de Eletrônica Digital 1", "FGA0073", 4, 20, 0),
    "ped1": MateriaSemPreRequisito("Prática de Eletrônica Digital 1", "FGA0071", 2, 0),
    "oo": Materia("Orientação a Objetos", "FGA0158", 4, 50, 0),
    "md1": Materia("Matemática Discreta 1", "FGA0085", 4, 12, 0),
    # 4 semestre
    "gpq": Materia("Gestão da Produção e Qualidade", "FGA0184", 4, 4, 0),
    "mds": Materia("Métodos de Desenvolvimento de Software", "FGA0138", 4, 38, 0),
    "ed1": Materia("Estrutura de Dados 1", "FGA0147", 4, 20, 0),
    "fac": Materia("Fundamentos de Arquitetura de Computadores", "FGA0142", 4, 16, 0),
    "md2": Materia("Matemática Discreta 2", "FGA0108", 4, 8, 0),
    "pi1": Materia("Projeto Integrador de Engenharia 1", "FGA0150", 4, 6, 0),
    # 5 semestre
    "ihc": Materia("Interação Humano Computador", "FGA0173", 4, 4, 0),
    "rs": Materia("Requisitos de Software", "FGA0172", 4, 18, 0),
    "sb1": Materia("Sistemas de Banco de Dados 1", "FGA0137", 4, 4, 0),
    "fso": Materia("Fundamentos de Sistemas Operacionais", "FGA0170", 4, 12, 0),
    "cp1": Materia("Compiladores 1", "FGA0003", 4, 4, 0),
    "eda2": Materia("Estrutura de Dados 2", "FGA0030", 4, 4, 0),
    # 6 semestre
    "qs1": MateriaSemPreRequisito("Qualidade de Software 1", "FGA0278", 4, 0),
    "ts": Materia("Testes de Software", "FGA0238", 4, 18, 0),
    "ads": Materia("Arquitetura e Desenho de Software", "FGA0208", 4, 14, 0),
    "frc": Materia("Fundamentos de Redes de Computadores", "FGA0211", 4, 4, 0),
    "sb2": MateriaSemPreRequisito("Sistemas de Banco de Dados 2", "FGA0060", 4, 0),
    "paa": MateriaSemPreRequisito("Projeto de Algoritmos", "FGA0124", 4, 0),
    # 7 semestre
    "tpe": Materia("Técnicas de Programação em Plataformas Emergentes", "FGA0242", 4, 10, 0),
    "pp": MateriaSemPreRequisito("Paradigmas de Programação", "FGA0210", 4, 0),
    "fse": MateriaSemPreRequisito("Fundamentos de Sistemas Embarcados", "FGA0109", 4, 0),
    "pspd": MateriaSemPreRequisito("Programação para Sistemas Paralelos e Distribuídos", "FGA0244", 4, 0),
    # 8 semestre
    "eps": Materia("Engenharia de Produto de Software", "FGA0206", 4, 6, 0),
    "gce": MateriaSemPreRequisito("Gerência de Configuração e Evolução de Software", "FGA0240", 4, 0),
    "es1": MateriaSemPreRequisito("Estágio Supervisionado 1", "FGA0021", 14, 0),
    # 9 semestre
    "pi2": MateriaSemPreRequisito("Projeto Integrador de Engenharia 2", "FGA0250", 6, 0),
    "tcc1": Materia("Trabalho de Conclusão de Curso 1", "FGA0009", 4, 6, 0),
    # 10 semestre
    "tcc2": MateriaSemPreRequisito("Trabalho de Conclusão de Curso 2", "FGA0011", 6, 0)
}